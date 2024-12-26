from DOMAIN.utils.sendRequest import send_request


def create_playlist(token, userID, name, isPrivate):
    create_playlist_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    create_playlist_json_data = {
        'name': name,
        'description': 'New playlist description',
        'public': isPrivate,
    }

    create_playlist_url = f"https://api.spotify.com/v1/users/{userID}/playlists"

    create_playlist_response = send_request("post", create_playlist_url, headers=create_playlist_headers, json_data=create_playlist_json_data)

    return create_playlist_response.json()
