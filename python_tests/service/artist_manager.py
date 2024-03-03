from service import mysql_manager
from entity.Artist import Artist


def find_artist_by_spotify_id(spotify_id):
    session = mysql_manager.Session()
    artist = session.query(Artist).filter(Artist.spotify_id == spotify_id).one_or_none()
    session.close()
    return artist

def save_artist(artist):
    session = mysql_manager.Session()
    session.add(artist)
    session.commit()
    saved_artist = session.query(Artist).filter(Artist.artist_id == artist.artist_id).one_or_none()
    session.close()
    return saved_artist

def find_artist_by_artist_id(artist_id):
    session = mysql_manager.Session()
    artist = session.query(Artist).filter(Artist.artist_id == artist_id).one_or_none()
    session.close()
    return artist

def spotify_response_to_artist(spotify_response):
    return Artist(
        name=spotify_response['name'],
        genres=str(spotify_response['genres']),
        spotify_id=spotify_response['id'],
        spotify_popularity=spotify_response['popularity'],
        image=spotify_response['images'][0]['url']
    )