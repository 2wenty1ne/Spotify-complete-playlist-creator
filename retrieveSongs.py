from sendRequest import send_request


def retrieve_songs_from_artist_id(token, artist_id):
    authed_headers = {'Authorization': f'Bearer {token}'}
    basic_parms = {'market': 'DE', 'limit': '50', 'offset': '0'}


    # ? Get artist name
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    artist_headers = authed_headers
    artist_params = {'market': 'DE'}

    artist_response = send_request("get", artist_url, headers=artist_headers, params=artist_params)
    artist_id = artist_response['id']
    print(f"Loaded artist: {artist_response['name']} \nId: {artist_response['id']} \n")


    # ? Get albums
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    albums_headers = authed_headers
    # albums_params = basic_parms['include_groups'] = 'album,single'
    albums_params = basic_parms
    albums_params['include_groups'] = 'single'

    albums_response = send_request("get", albums_url, headers=albums_headers, params=albums_params)

    song_uris = []
    print("\nAlbums:")

    for album in albums_response['items']:
        album_url = album['href']
        album_name = album['name']
        album_id = album['id']

        songs_url = f"{album['href']}/tracks"
        songs_headers = authed_headers
        songs_params = {'market': 'DE', 'offset': '0'}

        songs_response = send_request("get", songs_url, headers=songs_headers, params=songs_params)
        print(f"\nAlbumname: {album_name} - Amount of songs: {songs_response['total']}:")

        for song in songs_response['items']:
            song_name = song['name']
            song_uri = song['uri']
            print(f"Name: {song_name} - Uri: {song_uri}")

    """
    first_album = albums_response['items'][0]
    first_album_url = first_album['href']
    first_album_name = first_album['name']
    first_album_tracks_url = f"{first_album_url}/tracks"
    songs_headers = authed_headers
    songs_params = {'market': 'DE', 'offset': '0'}

    songs_response = send_request("get", first_album_tracks_url, headers=songs_headers, params=songs_params)
    first_song = songs_response['items'][0]
    first_song_name = first_song['name']
    first_song_uri = first_song['uri']
    """


