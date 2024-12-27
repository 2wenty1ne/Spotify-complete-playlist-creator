def validate_create_playlist_request(data):
    required_keys = {
        "playlistName": str,
        "artistID": str,
        "isPrivate": bool
    }

    for key, expected_type in required_keys.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False

    return True