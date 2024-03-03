from service.artist_album_manager import spotify_response_to_albumlist
from util_api import spotify_manager

albums = spotify_manager.get_albums(2023)
spotify_response_to_albumlist(albums)
