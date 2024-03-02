from util_api import spotify_manager


albums = spotify_manager.get_albums(2023)
for album in albums:
    for artist in album['artists']:
        if artist['name'] == '<NAME>':