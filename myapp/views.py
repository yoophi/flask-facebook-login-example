import facebook
import requests
from flask import Blueprint, request, redirect, url_for
from flask_login import current_user, login_required, logout_user, login_user

from myapp.config import FACEBOOK_DISCOVERY_URL, FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET
from myapp.database import db
from myapp.models import User

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Facebook Profile Picture:</p>"
            '<img src="{}" alt="Facebook profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Facebook Login</a>'


def get_google_provider_cfg():
    return requests.get(FACEBOOK_DISCOVERY_URL).json()


@main.route("/login")
def login():
    # Find out what URL to hit for Facebook login
    canvas_url = url_for('main.callback', _external=True, _scheme='https')
    perms = []

    # Use library to construct the request for Facebook login and provide
    # scopes that let you retrieve user's profile from Facebook
    graph_api = facebook.GraphAPI(version="3.1")
    request_uri = graph_api.get_auth_url(FACEBOOK_CLIENT_ID, canvas_url, perms)
    return redirect(request_uri)


@main.route("/login/callback")
def callback():
    # Get authorization code Facebook sent back to you
    code = request.args.get("code")

    graph = facebook.GraphAPI()
    resp = graph.get_access_token_from_code(
        code,
        url_for('main.callback', _external=True, _scheme='https'),
        FACEBOOK_CLIENT_ID,
        FACEBOOK_CLIENT_SECRET
    )
    access_token = resp['access_token']
    graph = facebook.GraphAPI(access_token=access_token)
    resp2 = graph.get_object('me', fields="id,name,email,picture{url}")

    unique_id = resp2['id']
    users_name = resp2['name']
    users_email = resp2['email']
    picture = resp2['picture']['data']['url']
    user = db.session.query(User).filter(User.sub == unique_id).first()
    if user is None:
        # Create a user in your db with the information provided
        # by Facebook
        user = User()
        user.sub = unique_id
        user.name = users_name
        user.email = users_email
        user.profile_pic = picture
        db.session.add(user)
        db.session.commit()

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("main.index"))


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
