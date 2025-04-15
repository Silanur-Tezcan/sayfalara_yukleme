from django.shortcuts import render
from .models import Video

def home(request):
    return render(request, 'videolar/home.html')

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videolar/video_list.html', {'videos': videos})
