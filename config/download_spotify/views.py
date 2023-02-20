from django.shortcuts import render
from pytube import YouTube
import os
import requests
import re
from bs4 import BeautifulSoup






def index(request):
    # name = 'polozhenie'
    # download_mp3(get_url_video(name))
    return render(request, 'download_spotify/index.html')


def download_mp3(url):
    """Принимает ссылку на страницу с плеером и скачивает .mp3 файл"""
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    file = video.download()
    file_name = yt.title
    os.rename(file, file_name + '.mp3')
    

def get_url_video(name):
    """Принимает поисковой запрос. Возвращает ссылку на страницу с просмотром видео"""
    find_video_url = 'https://www.youtube.com/results?search_query=' + name.strip().replace(' ', '+')
    watch_video_url='https://www.youtube.com/watch?v='
    r = requests.get(find_video_url)
    video_id = re.search(r'"videoId":\".+?\"', r.text)
    clean_video_id = re.search(r'\".{11}\"', video_id.group(0))
    return watch_video_url + clean_video_id.group(0).replace('"', '')
