import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_id = '0ef1370ce5544661afdaba8be1572a5f'
client_secret = '7f35c93e79f14c47896531882cb6133f'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_albums(year, limit=50):
    albums = []
    offset = 0
    total = None

    while total is None or len(albums) < total:
        results = spotify.search(q="year:"+year, type='album', limit=limit, offset=offset)
        if total is None:
            total = results['albums']['total']
        albums.extend(results['albums']['items'])
        offset += limit
        time.sleep(1)
    return albums

def get_artists(spotify_id):
    return spotify.artists(spotify_id)

