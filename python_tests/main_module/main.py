from service import artist_album_manager, track_manager, lyric_manager
from util_api import spotify_manager
from util_api import musixmatch_manager
from dto import SongDto

# Get Spotify Albums by year
# albums = spotify_manager.get_albums_by_year(2022)
# artist_album_manager.spotify_response_to_albumlist(albums)


# Get Lyrics from Musixmatch
musixmatch_manager.get_all_track_lyrics()