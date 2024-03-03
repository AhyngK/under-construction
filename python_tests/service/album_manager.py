from service import mysql_manager
from entity.Album import Album
from datetime import datetime


def save_album(album):
    session = mysql_manager.Session()
    session.add(album)
    session.commit()
    saved_album = session.query(Album).filter(Album.album_id == album.album_id).one_or_none()
    session.close()
    return saved_album


def find_album_by_spotify_id(spotify_id):
    session = mysql_manager.Session()
    album = session.query(Album).filter(Album.spotify_id == spotify_id).one_or_none()
    session.close()
    return album


def find_album_by_id(album_id):
    session = mysql_manager.Session()
    album = session.query(Album).filter(Album.album_id == album_id).one_or_none()
    session.close()
    return album

def spotify_response_to_album(spotify_response):
    return Album(
        name = spotify_response['name'],
        album_type = spotify_response['album_type'],
        total_tracks = spotify_response['total_tracks'],
        spotify_id = spotify_response['id'],
        cover_image = spotify_response['images'][0]['url'] if spotify_response['images'] else None,
        release_date = figure_date(spotify_response['release_date'])
    )

def figure_date(date_str):
    if len(date_str) == 4:
        return datetime.strptime(date_str, '%Y').date()
    elif len(date_str) == 7:
        return datetime.strptime(date_str, '%Y-%m').date()
    elif len(date_str) >= 10:
        return datetime.strptime(date_str[:10], '%Y-%m-%d').date()
    else:
        return None