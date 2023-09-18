# $ pip install pytube

import pytube
from pytube.cli import on_progress
import sys

url = "https://www.youtube.com/watch?v=yU4jHoWLGCk"

def download_video(url):
    try:
        yt = pytube.YouTube(url, on_progress_callback=on_progress, use_oauth=True,
        allow_oauth_cache=True)
        print("Trying to download " + yt.title)
        #print(yt.check_availability())
        video = yt.streams.filter(progressive=True).get_highest_resolution()
        #video = yt.streams.get_highest_resolution()
        print("Downloading...")
        video.download()
        print("Download complete")
    except:
        print("Error in download_video")
        sys.exit(1)

download_video(url)