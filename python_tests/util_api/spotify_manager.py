import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from service import track_manager

client_id = '0ef1370ce5544661afdaba8be1572a5f'
client_secret = '7f35c93e79f14c47896531882cb6133f'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_albums_by_year(year, limit=50):
    albums = []
    offset = 0
    total = None
    while total is None or len(albums) < total:
        results = spotify.search(q="year:" + str(year), type='album', limit=limit, offset=offset)
        print(results)
        if total is None:
            total = results['albums']['total']
        albums.extend(results['albums']['items'])
        offset += limit
        time.sleep(1)
    return albums


def get_albums_new():
    albums = []
    offset = 0
    total = None
    while total is None or len(albums) < total:
        results = spotify.search(q="tag:new", type='album', limit=50, offset=offset)
        if total is None:
            total = results['albums']['total']
        albums.extend(results['albums']['items'])
        offset += 50
        time.sleep(1)
    return albums


def get_artist(spotify_id):
    return spotify.artist(spotify_id)


def get_album(spotify_id):
    return spotify.album(spotify_id)


def get_track_from_album(album):
    album_data = spotify.album(album.spotify_id)
    for track in album_data['tracks']['items']:
        if track_manager.find_track_by_spotify_id(track['id']) is None:
            track_result = spotify.track(track['id'])
            track_manager.save_track(track_manager.spotify_response_to_track(track_result, album.album_id))