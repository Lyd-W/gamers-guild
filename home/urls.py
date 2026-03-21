from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BoardgameList.as_view(), name="home"),
]
