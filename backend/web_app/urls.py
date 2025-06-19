from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("sign-up", views.sign_up, name="sign_up"),
]
# This file defines the URL patterns for the web application.
