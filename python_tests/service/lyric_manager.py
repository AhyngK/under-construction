import json

from service import mysql_manager
from entity.Lyric import Lyric

synced_lyric_location = ""
normal_lyric_location = ""


def musixmatch_reqult_to_lyric(body, track_id):
    lyrics = []
    subtitles = json.loads(body['subtitle']['subtitle_body'])
    for i, subtitle in enumerate(subtitles):
        text = subtitle['text']
        start_time = subtitle['time']['total']
        if i < len(subtitles) - 1:
            end_time = subtitles[i + 1]['time']['total']
        else:
            end_time = start_time

        if(text != ""):
            lyrics.append(Lyric(
                track_id = track_id,
                start_time = start_time,
                end_time = end_time,
                content = text
            ))
    save_lyrics(lyrics)
    return


def save_lyrics(lyrics):
    session = mysql_manager.Session()
    for lyric in lyrics:
        session.add(lyric)
    session.commit()
    session.close()


def save_lyric(lyric):
    session = mysql_manager.Session()
    session.add(lyric)
    session.commit()
    saved_lyric = session.query(Lyric).filter(Lyric.lyric_id == Lyric.lyric_id).one_or_none()
    session.close()
    return saved_lyric


def is_lyric_exists_by_track_id(track_id):
    session = mysql_manager.Session()
    lyric = session.query(Lyric).filter(Lyric.track_id == track_id).first()
    session.close()
    return lyric is not None