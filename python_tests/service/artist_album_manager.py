from util_api import spotify_manager
from service import album_manager, artist_manager, mysql_manager
from entity.ArtistAlbum import ArtistAlbum


def spotify_response_to_albumlist(album_response):
    for album_data in album_response:
        # If current Album isn't in Database
        if album_manager.find_album_by_spotify_id(album_data['id']) is None:
            # Insert Album data into database
            album = album_manager.save_album(album_manager.spotify_response_to_album(album_data))
            artists = []
            # Check Artists in current Album
            for artist_data in album_data['artists']:
                # If current album's artist isn't in Database, call api and insert into database
                artist = artist_manager.find_artist_by_spotify_id(artist_data['id'])
                if artist is None:
                    artist_response = spotify_manager.get_artist(artist_data['id'])
                    artist = artist_manager.save_artist(artist_manager.spotify_response_to_artist(artist_response))
                artists.append(artist)
            for artist in artists:
                save_connection(artist.artist_id, album.album_id)
            spotify_manager.get_track_from_album(album)


def save_connection(artist_id, album_id):
    session = mysql_manager.Session()
    new_connection = ArtistAlbum(artist_id=artist_id, album_id=album_id)
    session.add(new_connection)
    session.commit()
    session.close()
    return new_connection


def find_artist_by_album(album_id):
    session = mysql_manager.Session()
    artist_album = session.query(ArtistAlbum).filter(ArtistAlbum.album_id == album_id).first()
    session.close()
    return artist_album.artist_id