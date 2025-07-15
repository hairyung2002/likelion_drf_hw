from django.urls import path
from .views import *
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.singer_list_create, name='singer_list_create'),
    path('<int:singer_id>/songs', views.song_read_create, name='song_list_create'),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('songs/<int:song_id>', views.song_detail_update_delete),
    path('tags/<str:tags_name>', views.find_tag),
]  