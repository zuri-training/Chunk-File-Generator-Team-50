from django.urls import path
from . import views

app_name = 'split_file'
urlpatterns = [
    path("", views.split_home, name='split_home'),
    path("csv/", views.split_csv, name='split_csv'),
    path("json/", views.split_json, name='split_json'),
]
