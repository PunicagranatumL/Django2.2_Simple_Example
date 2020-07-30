from django.urls import path
from . import views

app_name = 'extractseq'

urlpatterns = [
    path('',views.index,name='index'),
    path('extractseq/',views.extractseq,name='extractseq'),
]