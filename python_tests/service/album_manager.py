from datetime import datetime
from mysql_manager import MySQLManager
from entity.Album import Album


def save_albums(albums):
    session = MySQLManager.Session()
    for album in albums:
        new_album = Album(
            name=album['name'],
            album_type=album['album_type'],
            total_tracks=album['total_tracks'],
            spotify_id=album['id'],
            cover_image=album['images'][0]['url'] if album['images'] else None,
            release_date=figure_date(album['release_date'])
        )
        session.add(new_album)
    session.commit()
    session.close()


def figure_date(date_str):
    if len(date_str) == 4:
        return datetime.strptime(date_str, '%Y').date()
    elif len(date_str) == 7:
        return datetime.strptime(date_str, '%Y-%m').date()
    elif len(date_str) >= 10:
        return datetime.strptime(date_str[:10], '%Y-%m-%d').date()
    else:
        return None
