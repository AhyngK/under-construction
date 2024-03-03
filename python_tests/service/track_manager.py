from service import mysql_manager, lyric_manager
from entity.Track import Track


def save_track(track):
    session = mysql_manager.Session()
    session.add(track)
    session.commit()
    session.close()
    return track


def find_track_by_spotify_id(spotify_id):
    session = mysql_manager.Session()
    track = session.query(Track).filter(Track.spotify_id == spotify_id).one_or_none()
    session.close()
    return track


def find_track_by_id(track_id):
    session = mysql_manager.Session()
    track = session.query(Track).filter(Track.track_id == track_id).one_or_none()
    session.close()
    return track


def spotify_response_to_track(spotify_response, album_id):
    return Track(
        name = spotify_response['name'],
        spotify_id = spotify_response['id'],
        album_id = album_id,
        track_number = spotify_response['track_number'],
        spotify_popularity = spotify_response['popularity'],
        duration_ms = spotify_response['duration_ms']
    )


def get_all_track_ids():
    session = mysql_manager.Session()
    query = session.query(Track.track_id).all()
    session.close()
    track_ids = [id[0] for id in query]
    return track_ids


def update_track_is_lyric(track_id):
    session = mysql_manager.Session()
    try:
        track = session.query(Track).filter(Track.track_id == track_id).one_or_none()
        if track and not track.is_lyrics and lyric_manager.is_lyric_exists_by_track_id(track_id):
            track.is_lyrics = True
            session.commit()
            print(f"[TRACK_MANAGER] : {track_id} is_lyrics updated to True.")
        elif track and track.is_lyrics:
            print(f"[TRACK_MANAGER] : {track_id} already has is_lyrics set to True.")
        else:
            print(f"[TRACK_MANAGER] : No Track found with ID {track_id} or no lyrics exist.")
    except Exception as e:
        session.rollback()
        print(f"[TRACK_MANAGER] : An error occurred: {e}")
    finally:
        session.close()

