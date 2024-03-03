from service import track_manager, artist_manager, album_manager, artist_album_manager
class SongDto:
    def __init__(
            self, album: str = "",
            artist: str = "",
            track_name: str = "",
            track_spotify_id: str = "",
            track_duration: int = 0
    ):
        self.album = album
        self.artist = artist
        self.track_name = track_name
        self.track_spotify_id = track_spotify_id
        self.track_duration = track_duration


def make_song_dto(track):
    album = album_manager.find_album_by_id(track.album_id)
    artist = artist_manager.find_artist_by_artist_id(artist_album_manager.find_artist_by_album(album.album_id))
    return SongDto(
        album = album.name,
        artist = artist.name,
        track_name = track.name,
        track_spotify_id = track.spotify_id,
        track_duration = track.duration_ms
    )