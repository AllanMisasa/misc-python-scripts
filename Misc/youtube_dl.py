'''
This script is used to download videos from YouTube
'''
import ffmpeg
import os
import sys
import pytube
from pytube.cli import on_progress

def download_video(url, resolution):
    '''Download a video from YouTube'''
    try:
        yt = pytube.YouTube(url=url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print("Trying to download " + yt.title)
        video = yt.streams.filter(res=resolution).first()
        print("Downloading...", video)
        video.download()
        print("Download complete")
        return yt.title
    except:
        print("Error in download_video")
        sys.exit(1)

def download_audio(url):
    '''Download the audio from a video'''
    try:
        yt = pytube.YouTube(url=url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print("Trying to download " + yt.title)
        audio = yt.streams.filter(only_audio=True, abr="160kbps").first()
        print("Downloading...", audio)
        audio.download()
        print("Download complete")
    except:
        print("Error in download_audio")
        sys.exit(1)

def combine_audio_video(video, audio, output="output.mp4"):
    try:
        video = ffmpeg.input(video)
        audio = ffmpeg.input(audio)
        ffmpeg.output(video, audio, output).run()
    except:
        print("Error in combine_audio_video")
        sys.exit(1) 

base_path="/home/janus/Documents/GitHub/misc-python-scripts/"
url = "https://www.youtube.com/watch?v=iaJVP67iU1Y"
name = download_video(url, resolution="1080p")
video_path = name.replace("|", "").replace(":", "").replace("*", "").replace(".", "").replace(",", "")
#video_path = video_path.replace(":", "")
#video_path = video_path.replace("*", "")
#video_path = video_path.replace(".", "")
#video_path = video_path.replace(",", "")
path = base_path + video_path
download_audio(url)
combine_audio_video(path+".mp4", path+".webm", path+"_f.mp4")