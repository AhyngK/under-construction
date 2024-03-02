from mysql_manager import MySQLManager
from entity.Artist import Artist


def find_artist(spotify_id):
    session = MySQLManager.Session()
    artist = session.query(Artist).filter(Artist.spotify_id == spotify_id).first()
    session.close()
    return artist
