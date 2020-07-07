from django.urls import path
from . import views

app_name = 'youtube_download'

urlpatterns = [
    path('',views.index,name='index'),
    path('ytb_main/',views.ytb_main,name='ytb_main'),
    path('ytb_download/',views.ytb_download,name='ytb_download'),
    path('download_complete/<res>',views.download_complete,name='download_complete'),
]