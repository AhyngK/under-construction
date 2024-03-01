import argparse
import json
import logging
import math
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import requests

# https://github.com/fashni/MxLRC/blob/main/mxlrc.py
# https://spicetify.app/docs/faq/#sometimes-popup-lyrics-andor-lyrics-plus-seem-to-not-work

class SyncedLyrics :
    def __init__(self, token):
        self.base_url = "https://apic-desktop.musixmatch.com/ws/1.1/"
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def find_lyrics(self, song):
        durr = song.duration / 1000 if song.duration else ""
        params = {
            "q_album": song.album,
            "q_artist": song.artist,
            "q_artists": song.artist,
            "q_track": song.title,
            "track_spotify_id": song.uri,
            "q_duration": durr,
            "f_subtitle_length": math.floor(durr) if durr else "",
            "usertoken": self.token,
        }

        req = urllib.request.Request(self.base_url + urllib.parse.urlencode(params, quote_via=urllib.parse.quote),
                                     headers=self.headers)
        try:
            response = urllib.request.urlopen(req).read()
        except (urllib.error.HTTPError, urllib.error.URLError, ConnectionResetError) as e:
            logging.error(repr(e))
            return

        r = json.loads(response.decode())
        if r['message']['header']['status_code'] != 200 and r['message']['header'].get('hint') == 'renew':
            logging.error("Invalid token")
            return
        body = r["message"]["body"]["macro_calls"]

        if body["matcher.track.get"]["message"]["header"]["status_code"] != 200:
            if body["matcher.track.get"]["message"]["header"]["status_code"] == 404:
                logging.info('Song not found.')
            elif body["matcher.track.get"]["message"]["header"]["status_code"] == 401:
                logging.warning('Timed out. Change the token or wait a few minutes before trying again.')
            else:
                logging.error(f'Requested error: {body["matcher.track.get"]["message"]["header"]}')
            return
        elif isinstance(body["track.lyrics.get"]["message"].get("body"), dict):
            if body["track.lyrics.get"]["message"]["body"]["lyrics"]["restricted"]:
                logging.info("Restricted lyrics.")
                return
        return body


if __name__ == "__main__":
    # Musixmatch API 토큰을 여기에 입력하세요.
    token = "YOUR_MUSIXMATCH_API_TOKEN"
    track_id = "TRACK_ID"  # 찾고자 하는 트랙의 ID를 여기에 입력하세요.

    musixmatch = SyncedLyrics(token)
    lyrics = musixmatch.find_synced_lyrics(track_id)

    if lyrics:
        print("동기화된 가사:\n", lyrics)