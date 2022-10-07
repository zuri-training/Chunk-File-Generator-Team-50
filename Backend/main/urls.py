from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutUs, name="about"),
    path("faq/", views.FaQ, name="faq"),
    path("contact/", views.contact, name="contact"),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('profile/', views.profile, name='profile'),
    ]
#if settings.DEBUG:
    #creates a last urlpattern - with the media url, so, whatever path is in the media_url is made a url pattern
    #
        #urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
