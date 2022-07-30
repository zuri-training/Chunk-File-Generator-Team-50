from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.home, name="home"),
    path('documentation', views.documentation, name='documentation'),
    path("new_features/", views.features, name="features"),
    ]
#if settings.DEBUG:
    #creates a last urlpattern - with the media url, so, whatever path is in the media_url is made a url pattern
    #
        #urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
