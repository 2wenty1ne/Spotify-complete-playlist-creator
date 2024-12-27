import base64

from DOMAIN.secretAccess.userData import get_client_id, get_client_secret
from DOMAIN.utils.sendRequest import send_request


client_id = get_client_id()
client_secret = get_client_secret()


def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
    data = {'grant_type': 'client_credentials'}

    token = send_request("post", url, headers=headers, data=data)['access_token']

    if token:
        print("Got token \n")
        return token
    else:
        print("Error receiving the token")
        return 0
