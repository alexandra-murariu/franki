import time
import pyperclip
from threading import Thread
from franki.wordminer import subtitle_queue

_seen = set()


def watch_clipboard():
    def _watch():
        last = ""
        while True:
            text = pyperclip.paste().strip()
            if text and text != last and text not in _seen:
                subtitle_queue.append(text)
                _seen.add(text)
                last = text
            time.sleep(0.25)

    Thread(target=_watch, daemon=True).start()


def process_subtitles(callback):
    def _loop():
        while True:
            if subtitle_queue:
                subtitle = subtitle_queue.popleft()
                callback(subtitle)
            else:
                time.sleep(0.1)

    Thread(target=_loop, daemon=True).start()