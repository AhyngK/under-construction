import json
import logging
import math
import urllib.error
import urllib.parse
import urllib.request
import time

from dto import SongDto
from service import track_manager, lyric_manager

token = "2403039f928c7ac6143d9e74dd8297d28cfb25348a0f94fd5c7002"
base_url = "https://apic-desktop.musixmatch.com/ws/1.1/macro.subtitles.get?format=json&namespace=lyrics_richsynched&subtitle_format=mxm&app_id=web-desktop-app-v1.0&"
headers = {"authority": "apic-desktop.musixmatch.com", "cookie": "x-mxm-token-guid="}


def get_track_lyrics(track_id):
    track = track_manager.find_track_by_id(track_id)
    song = SongDto.make_song_dto(track)
    return find_lyrics(song)


def get_all_track_lyrics():
    track_ids = track_manager.get_all_track_ids()
    for id in track_ids:
        if not lyric_manager.is_lyric_exists_by_track_id(id):
            body = get_track_lyrics(id)
            lyric_manager.musixmatch_reqult_to_lyric(body, id)
        track_manager.update_track_is_lyric(id)
        time.sleep(5)


def find_lyrics(songDto:SongDto):
    duration = songDto.track_duration / 1000 if songDto.track_duration else ""
    params = {
        "q_album": songDto.album,
        "q_artist": songDto.artist,
        "q_artists": songDto.artist,
        "q_track": songDto.track_name,
        "track_spotify_id": songDto.track_spotify_id,
        "q_duration": duration,
        "f_subtitle_length": math.floor(duration) if duration else "",
        "usertoken": token,
    }

    req = urllib.request.Request(base_url + urllib.parse.urlencode(params, quote_via=urllib.parse.quote),
                                 headers=headers)
    try:
        response = urllib.request.urlopen(req).read()
    except (urllib.error.HTTPError, urllib.error.URLError, ConnectionResetError) as e:
        logging.error(repr(e))
        return

    r = json.loads(response.decode())
    if r['message']['header']['status_code'] != 200 and r['message']['header'].get('hint') == 'renew':
        logging.error("[MUSIXMATCH LOG] : Invalid token")
        return
    body = r["message"]["body"]["macro_calls"]

    if body["matcher.track.get"]["message"]["header"]["status_code"] != 200:
        if body["matcher.track.get"]["message"]["header"]["status_code"] == 404:
            logging.info('Song not found.')
        elif body["matcher.track.get"]["message"]["header"]["status_code"] == 401:
            logging.warning('[MUSIXMATCH LOG] : Timed out. Change the token or wait a few minutes before trying again.')
        else:
            logging.error(f'Requested error: {body["matcher.track.get"]["message"]["header"]}')
        return
    elif isinstance(body["track.lyrics.get"]["message"].get("body"), dict):
        if body["track.lyrics.get"]["message"]["body"]["lyrics"]["restricted"]:
            logging.info("[MUSIXMATCH LOG] : Restricted lyrics.")
            return
    elif body["matcher.track.get"]["message"]["body"]["track"]["has_richsync"] == 0:
        logging.info("[MUSIXMATCH LOG] : No richsync found.")
        return
    print("로그"+str(body['track.subtitles.get']['message']['body']['subtitle_list'][0]))
    return body['track.subtitles.get']['message']['body']['subtitle_list'][0]