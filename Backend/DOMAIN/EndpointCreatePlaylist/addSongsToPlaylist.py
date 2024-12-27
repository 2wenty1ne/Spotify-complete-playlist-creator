import json

from DOMAIN.requestHandling.sendRequest import send_request


def addSongsToPlaylist(accessToken, playlistID, songsToAdd):
    chunkSize = 100

    for songIndex in range(0, len(songsToAdd), chunkSize):
        chunk = songsToAdd[songIndex:songIndex + chunkSize]
        addOneChunkToPlaylist(accessToken, playlistID, chunk)


def addOneChunkToPlaylist(accessToken, playlistID, songChunk):
    add_songs_headers = {
        'Authorization': f'Bearer {accessToken}',
        'Content-Type': 'application/json',
    }
    
    add_songs_data = {
        "uris": songChunk,
        "position": 0
    }

    add_songs_url = f"https://api.spotify.com/v1/playlists/{playlistID}/tracks"

    create_playlist_response = send_request("post", add_songs_url, headers=add_songs_headers, json_data=add_songs_data)
    
    return create_playlist_response
