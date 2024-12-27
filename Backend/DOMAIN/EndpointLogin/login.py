import random
import string
import urllib
from flask import redirect, request


def loginResponse(CLIENT_ID, SCOPE, STATE_KEY_COOKIE):
    state = generate_random_string(16)

    host = request.host_url.rstrip('/')
    redirect_uri = f"{host}/callback"

    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': SCOPE,
        'redirect_uri': redirect_uri,
        'state': state
    }

    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)

    response = redirect(url)
    response.set_cookie(STATE_KEY_COOKIE, state) #? Lasts as long as the browser session

    return response


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
