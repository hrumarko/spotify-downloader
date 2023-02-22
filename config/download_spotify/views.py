from django.shortcuts import render
from django.http import  HttpResponse
from django.core.files import File as DjangoFile
from .forms import GetTitleForm
from pytube import YouTube
from .models import File
import json
import os
import requests
import re


def index(request):
    form = GetTitleForm()
    if request.method == 'POST':
        form = GetTitleForm(request.POST)
        title = request.POST.get('title')
        if form.is_valid():
            id_video = get_url_video(title)[-11::]
            print(id_video)
            if File.objects.filter(id_video=id_video):
                return download_file_from_db(id_video)
            else:
                print('hello')
                file_path = download_mp3(get_url_video(title))
                file_buffer = open(file_path, "rb").read()
                response = HttpResponse(file_buffer)
                response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
                return response
    ctx = {
            'form': form,
            'chart': chart,
            }
    return render(request, 'download_spotify/index.html', ctx)


def chart(request):
    country = get_client_ip(request)
    chart = File.objects.filter(country=country)
    print(chart)
    if request.method == 'POST':
        id = request.POST.get('id')
        return download_file_from_db(id)
    ctx = {
            'chart': chart,
            }
    return render(request, 'download_spotify/chart.html', ctx)

    

def download_mp3(url, country='', is_chart=False):
    """Принимает ссылку на страницу с плеером и скачивает .mp3 файл"""
    yt = YouTube(url)
    file_name = yt.title
    video = yt.streams.filter(only_audio=True).first()
    file = video.download()
    mp3 = DjangoFile(open(file, mode='rb'), name=file_name + '.mp3')
    file_name = file_name.replace('Video', 'Audio')
    filik = File.objects.create(title=file_name, id_video=url[-11::], file=mp3, is_chart=is_chart, country=country)
    os.remove(file)
    return filik.file.path



def get_url_video(name):
    """Принимает поисковой запрос. Возвращает ссылку на страницу с просмотром видео"""
    print(name)
    find_video_url = 'https://www.youtube.com/results?search_query=' + name.strip().replace(' ', '+')
    watch_video_url='https://www.youtube.com/watch?v='
    r = requests.get(find_video_url)
    with open('page.html', 'w') as fl:
        fl.write(r.text)
    video_id = re.search(r'"videoRenderer":{"videoId":\".+?\"', r.text)
    clean_video_id = re.search(r'\".{11}\"', video_id.group(0))
    return watch_video_url + clean_video_id.group(0).replace('"', '')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    API_KEY = '99d4710e03d745ba8f0ec523bc9110a2'
    api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + API_KEY
    
    test_ip ='103.215.219.255' # ukraine

    response = requests.get(api_url + "&ip_address=" + test_ip)
    ip_dict = json.loads(response.text)
    country = ip_dict['country']
    return country


def download_file_from_db(id_video):
    file = File.objects.get(id_video=id_video)
    file_path = file.file.path
    file_buffer = open(file_path, "rb").read()
    response = HttpResponse(file_buffer)
    response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
    return response


def upadate_charts(tracks):
    country = tracks[0]
    for i in range(47, len(tracks)):
        id_video = get_url_video(tracks[i])[-11::]
        if not File.objects.filter(id_video=id_video):
            download_mp3(get_url_video(tracks[i]), country, True)


def get_charts(country):
    CHART_API_KEY = 'fd628dc7e1687dc445ec43692e2021f9'
    url = f'http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks&country={country}&api_key={CHART_API_KEY}&format=json'
    chart_response = requests.get(url)
    chart_dict = json.loads(chart_response.text)
    tracks = []
    tracks.append(country)
    for i in chart_dict['tracks']['track']:
        tracks.append(i['name'] + ' ' + i['artist']['name'])
    return tracks 
