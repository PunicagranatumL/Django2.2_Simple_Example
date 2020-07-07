from django.shortcuts import render
from django.shortcuts import redirect

import os
from pytube import YouTube

# Create your views here.

def index(request):
    return render(request,'index.html')

def ytb_main(request):
    return render(request,'ytb_main.html')

def ytb_download(request):
    global url
    url = request.GET.get('url')
    print(url)
    try:
        obj = YouTube(url)
        resolutions = []
        strm_all = obj.streams.filter(progressive=True,file_extension='mp4').all()
        for i in strm_all:
            resolutions.append(i.resolution)
        print(resolutions)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = url.replace("watch?v=","embed/")
        context = {
            'rsl':resolutions,
            'embed_link':embed_link,
        }
        return render(request,'ytb_download.html',context=context)
    except:
        return render(request,'sorry.html')


def download_complete(request,res):
    global url
    print(res)
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    print(homedir)
    print(f'DIRECT:',f'{dirs}/Downloads')
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(res).download(dirs)
        return render(request,'download_complete.html')
    else:
        return redirect("youtube_download:ytb_main")