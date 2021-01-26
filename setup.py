#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'requests==2.21.0',
    'Flask==1.1.2',
    'Flask-Login==0.4.1',
    'Flask-Sqlalchemy==2.4.4',
    'SQLAlchemy==1.3.22',
    'facebook-sdk==3.1.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Pyunghyuk Yoo",
    author_email='yoophi@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Flask Google Login Sample",
    entry_points={
        'console_scripts': [
            'myapp=myapp.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='myapp',
    name='myapp',
    packages=find_packages(include=['myapp', 'myapp.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yoophi/app',
    version='0.1.0',
    zip_safe=False,
)
