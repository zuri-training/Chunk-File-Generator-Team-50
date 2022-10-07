from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("profile/", views.dashboard, name="profile"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name='register')
]
