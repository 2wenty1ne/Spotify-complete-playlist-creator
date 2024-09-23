from utils.sendRequest import send_request
from data.userData import get_user_id


def create_playlist(token):
    user_id = get_user_id()

    authed_headers = {'Authorization': f'Bearer {token}'}

    create_playlist_headers = authed_headers
    create_playlist_headers['Content-Type'] = 'application/json'

    create_playlist_json_data = {'name': 'Amogus','description': 'Amogus','public': False}

    create_playlist_url = f"https://api.spotify.com/v1/users/[{user_id}/playlists"

    send_request("post", create_playlist_url, headers=create_playlist_headers, json_data=create_playlist_json_data)



    # response = requests.post('https://api.spotify.com/v1/users/thedarkvic/playlists', headers=headers, json=json_data)

