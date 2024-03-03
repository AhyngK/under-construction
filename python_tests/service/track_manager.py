from service import mysql_manager
from entity.Track import Track


def save_track(track):
    session = mysql_manager.Session()
    session.add(track)
    session.commit()
    session.close()
    return track

def find_track(spotify_id):
    session = mysql_manager.Session()
    track = session.query(Track).filter(Track.spotify_id == spotify_id).first()
    session.close()
    return track