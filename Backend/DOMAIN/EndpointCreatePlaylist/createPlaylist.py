from DOMAIN.requestHandling.sendRequest import send_request


def create_playlist(token, userID, name, isPrivate):

    create_playlist_json_data = {
        'name': name,
        'description': 'New playlist description',
        'public': isPrivate,
    }

    create_playlist_url = f"https://api.spotify.com/v1/users/{userID}/playlists"

    create_playlist_response = send_request("post", create_playlist_url, token, json_data=create_playlist_json_data)

    return create_playlist_response.json()
