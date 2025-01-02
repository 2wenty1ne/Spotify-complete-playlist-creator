from DOMAIN.dataClasses.Song import Song
from DOMAIN.requestHandling.sendRequest import send_request, clear_whitespaces


def retrieve_songs_from_artist_id(token, artist_id):
    basic_parms = {'market': 'DE', 'limit': '50', 'offset': '0'}


    # ? Get artist name
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    artist_params = {'market': 'DE'}

    artist_response = send_request("get", artist_url, token, params=artist_params).json()
    artist_id = artist_response['id']


    # ? Get all albums
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    albums_params = basic_parms
    albums_params['include_groups'] = 'album, single'
    # albums_params['include_groups'] = 'album'
    albums_params = clear_whitespaces(albums_params)
    albums_response = send_request("get", albums_url, token, params=albums_params).json()


    #? Get every album
    song_list = []

    for album in albums_response['items']:
        album_url = album['href']

        songs_url = f"{album_url}/tracks"
        songs_params = {'market': 'DE', 'offset': '0'}

        songs_response = send_request("get", songs_url, token, params=songs_params).json()

        #? Get every song on an album
        for curr_song in songs_response['items']:
            song = Song(curr_song['name'], curr_song['uri'], album['name'], album['album_type'], curr_song['track_number'], artist_id, [])

            for artist in curr_song['artists']:
                song.artist_ids.append(artist['id'])

            add_songs_to_list(song_list, song)

    print(f"\n{len(song_list)} Songs added \n") #! TEST
    return song_list


def add_songs_to_list(song_list, new_song):
    if not song_list:
        if is_main_artist_present(new_song):
            song_list.append(new_song)
        return

    is_double = False
    for compare_song in song_list:
        if compare_song.name == new_song.name:
            is_double = True

    if not is_double:
        if is_main_artist_present(new_song):
            song_list.append(new_song)


def is_main_artist_present(song):
    if song.main_artist_id in song.artist_ids:
        return True
    else:
        return False
