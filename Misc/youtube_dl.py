'''
This script is used to download videos from YouTube
'''
import ffmpeg
import os
import sys
import pytube
from pytube.cli import on_progress

def download_video(url, resolution):
    try:
        yt = pytube.YouTube(url=url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print("Trying to download " + yt.title)
        video = yt.streams.filter(only_video=True, res=resolution).order_by('resolution').desc().first()
        print("Downloading...", video)
        video.download()
        print("Download complete")
        return yt.title
    except Exception as e:
        print("Error in download_video", e)
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
    except Exception as e:
        print("Error in download_audio", e)
        sys.exit(1)

def combine_audio_video(video, audio, output="output.mp4"):
    try:
        video = ffmpeg.input(video)
        audio = ffmpeg.input(audio)
        ffmpeg.output(video, audio, output).run()
    except Exception as e:
        print("Error in combine_audio_video", e)
        sys.exit(1) 

base_path="/home/janus/repos/misc-python-scripts/"
url = "https://www.youtube.com/watch?v=j6f8MrpCz34"
name = download_video(url, resolution="1440p")
video_path = name.replace("|", "").replace(":", "").replace("*", "").replace(".", "").replace(",", "")
path = base_path + video_path
download_audio(url)
combine_audio_video(path+".mp4", path+".webm", path+"_f.mp4")
