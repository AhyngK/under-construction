from service import mysql_manager
from entity.Album import Album


def save_album(album):
    session = mysql_manager.Session()
    session.add(album)
    session.commit()
    saved_album = session.query(Album).filter(Album.album_id == album.album_id).first()
    session.close()
    return saved_album


def find_album_by_spotify_id(spotify_id):
    session = mysql_manager.Session()
    album = session.query(Album).filter(Album.spotify_id == spotify_id).first()
    session.close()
    return album