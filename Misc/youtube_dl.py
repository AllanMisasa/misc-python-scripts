'''
This script is used to download videos from YouTube
'''

import sys
import pytube
from pytube.cli import on_progress

def download_video(url, res='1440p'):
    '''Download a video from YouTube'''
    try:
        yt = pytube.YouTube(url=url, on_progress_callback=on_progress, use_oauth=True,
        allow_oauth_cache=True)
        print("Trying to download " + yt.title)
        video = yt.streams.filter(res=res).first()
        print("Downloading...")
        video.download()
        print("Download complete")
    except:
        print("Error in download_video")
        sys.exit(1)

url = "https://www.youtube.com/watch?v=FfcIKP2bscQ"
download_video(url, '1080p')