from service import mysql_manager
from entity.Artist import Artist

from util_api import spotify_manager


def find_artist_by_spotify_id(spotify_id):
    session = mysql_manager.Session()
    artist = session.query(Artist).filter(Artist.spotify_id == spotify_id).first()
    session.close()
    return artist

def save_artist(artist):
    session = mysql_manager.Session()
    session.add(artist)
    session.commit()
    saved_artist = session.query(Artist).filter(Artist.artist_id == artist.artist_id).one()
    session.close()
    return saved_artist
