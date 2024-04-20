from Song import Song
from sendRequest import send_request, clear_whitespaces


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


    # ? Get all albums
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    albums_headers = authed_headers
    albums_params = basic_parms
    albums_params['include_groups'] = 'album, single'
    # albums_params['include_groups'] = 'album'
    albums_params = clear_whitespaces(albums_params)
    albums_response = send_request("get", albums_url, headers=albums_headers, params=albums_params)


    #? Get every album
    song_list = []
    # print("\nAlbums:") # TEST
    for album in albums_response['items']:
        album_url = album['href']

        # songs_url = f"{album_url}/tracks"
        haftbefehl_test_album_id = "2irGlvjYWIG5mtVwlahBu3"
        songs_url = f"https://api.spotify.com/v1/albums/{haftbefehl_test_album_id}/tracks"
        songs_headers = authed_headers
        songs_params = {'market': 'DE', 'offset': '0'}

        songs_response = send_request("get", songs_url, headers=songs_headers, params=songs_params)

        #? Get every song on an album
        for curr_song in songs_response['items']:
            song = Song(curr_song['name'], curr_song['uri'], album['name'], album['album_type'], curr_song['track_number'], artist_id, [])

            for artist in curr_song['artists']:
                song.artist_ids.append(artist['name'])

            add_songs_to_list(song_list, song)

    print("\nAfter song addition")

    print(f"\n{len(song_list)} Songs added \n")


def add_songs_to_list(song_list, new_song):
    # print(f"Checking: {new_song.name = }, number: {new_song.tracknumber} from {new_song.album_type} - {new_song.album}") # TEST
    print(new_song)
    if not song_list:
        song_list.append(new_song)
        return

    is_double = False
    for compare_song in song_list:
        if compare_song.name == new_song.name:
            is_double = True

    # print(f"{is_double = }\n") # TEST

    if not is_double:
        song_list.append(new_song)


def check_if_artist_is_present(song):
    pass
