from django.shortcuts import redirect, render,HttpResponse
from pytube import YouTube, streams
global video,link

def load_index(request):
    return render(request,'index.html',{'res':"",'url':""})

def load_info(request):
    
    global video,link
    if "https://www.youtube.com/" in request.POST.get('url'):
        link = request.POST['url']
        video = YouTube(link)
        stream = []
        
        for x in video.streams.filter(adaptive=True):
            size = "{:.3f}".format(x.filesize / 1020 ** 2)
            if x.type == "video" and x.mime_type == "video/mp4":
                stream.append((x.itag,x.resolution,size))
            elif x.type == "audio":
                stream.append((x.itag,x.abr,size))
        return render(request,'index.html',{'res':stream,'url':link})
    else:
        return render(request,'index.html',{'info':"Please enter youtube video url",'url':link})
    
def download_video(request):
    global video,link
    if request.POST.get('video_res'):
        stream = video.streams.get_by_itag(request.POST.get('video_res')).url
        return render(request,'index.html',{"Show":True,'url1':stream,'url':link,'res':"",'Note':"Click below to download"})
    else:
        return render(request,'index.html',{'info':"Please select youtube video quality",'url':link})
