from service import mysql_manager
from datetime import datetime
from sqlalchemy.orm import joinedload

from util_api import spotify_manager

from service import album_manager, artist_manager

from entity.Album import Album
from entity.Artist import Artist
from entity.ArtistAlbum import ArtistAlbum

def spotify_response_to_albumlist(album_response):
    for album_data in album_response:
        # If current Album isn't in Database
        if album_manager.find_album_by_spotify_id(album_data['id']) is None:
            artists = []
            # Check Artists in current Album
            for artist_data in album_data['artists']:
                # If current album's artist isn't in Database, call api and insert into database
                artist = artist_manager.find_artist_by_spotify_id(artist_data['id'])
                if artist is None:
                    artist_response = spotify_manager.get_artist(artist_data['id'])
                    artist = Artist(
                        name = artist_response['name'],
                        spotify_id = artist_response['id'],
                        spotify_popularity = artist_response['popularity'],
                        image = artist_response['images'][0]['url']
                    )
                    artist = artist_manager.save_artist(artist)
                artists.append(artist)
            # Insert Album data into database
            album = Album(
                name = album_data['name'],
                album_type = album_data['album_type'],
                total_tracks = album_data['total_tracks'],
                spotify_id = album_data['id'],
                cover_image = album_data['images'][0]['url'] if album_data['images'] else None,
                release_date = figure_date(album_data['release_date'])
            )
            album = album_manager.save_album(album)
            print("로그 : Album "+str(album))
            print("로그 : Artist "+str(artists))
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


def figure_date(date_str):
    if len(date_str) == 4:
        return datetime.strptime(date_str, '%Y').date()
    elif len(date_str) == 7:
        return datetime.strptime(date_str, '%Y-%m').date()
    elif len(date_str) >= 10:
        return datetime.strptime(date_str[:10], '%Y-%m-%d').date()
    else:
        return None
