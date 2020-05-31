from django.urls import path
from . import views

app_name = 'entries'

urlpatterns = [
    path('',views.HomeView.as_view(),name='blog-home'),
    path('detail/<int:pk>/',views.EntryView.as_view(),name="entry-detail"),
    path('create_entry/',views.CreateEntryView.as_view(success_url='/entries/'),name='create_entry'),
]