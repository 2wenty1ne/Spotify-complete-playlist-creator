import os
import string
import random
import urllib.parse
from flask import Flask, redirect, request, render_template

from secretAccess.userData import get_client_id


CLIENT_ID = get_client_id()
WEB_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'node_project'))
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
STATE = ""

app = Flask(__name__, template_folder=WEB_FOLDER_PATH, static_folder=WEB_FOLDER_PATH)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


@app.route('/')
def home():
    homeTemplatePath = "home/home.html"
    return render_template(homeTemplatePath)


@app.route('/login')
def login():
    STATE = generate_random_string(16)
    print(f"State in login: {STATE} \n\n")
    scope = 'user-read-private user-read-email'

    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': STATE
    }

    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
    print(f"redirect url: {url}")
    return redirect(url)


@app.route('/callback')
def callback():
    print(f"State in callback: {STATE} \n\n")
    return render_template('login-callback/login-callback.html')


if __name__ == '__main__':
    app.run(port=8888, debug=True)