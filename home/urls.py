from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BoardgameList.as_view(), name="home"),
    path("<slug:slug>/", views.boardgame_detail, name="boardgame_detail"),
]
