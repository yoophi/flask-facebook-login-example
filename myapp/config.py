import os

FACEBOOK_CLIENT_ID = os.environ.get("FACEBOOK_CLIENT_ID", None)
FACEBOOK_CLIENT_SECRET = os.environ.get("FACEBOOK_CLIENT_SECRET", None)
FACEBOOK_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
