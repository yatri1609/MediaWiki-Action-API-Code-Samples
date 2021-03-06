#!/usr/bin/python3

"""
    move.py

    MediaWiki Action API Code Samples
    Demo of `Move` module: Move a page with its
    talk page, leaving a redirect behind.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: Send a POST request to log in. For this login
# method, obtain credentials by first visiting
# https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "login",
    "lgname": "user_name",
    "lgpassword": "password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)
DATA = R.json()

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a POST request to move the page
PARAMS_4 = {
    "action": "move",
    "format": "json",
    "from": "Current title",
    "to": "Page with new title",
    "reason": "Typo",
    "movetalk": "1",
    "noredirect": "1",
    "token": CSRF_TOKEN
}

R = S.post(url=URL, data=PARAMS_4)
DATA = R.text

print(DATA)
