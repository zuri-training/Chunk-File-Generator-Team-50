from django.urls import path
from . import views

app_name = 'split_file'
urlpatterns = [
    path("", views.split_home, name='split_home'),
    path("uploadcsv/", views.upload_csv, name='uploadcsv'),
    path("splitcsv/", views.split_csv, name='splitcsv'),
    path("downloadcsv/", views.download_csv, name='downloadcsv'),
    path("savecsv/", views.save_csv, name='savecsv'),
    path("savedcsvlist/", views.saved_csv_list, name='savedcsvlist'),
    path("json/", views.split_json, name='split_json'),
]
