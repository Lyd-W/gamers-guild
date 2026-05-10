from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("search/", views.search, name="search"),
    path("<slug:slug>/favourite/", views.toggle_favourite, 
         name="toggle_favourite"),
    path("<slug:slug>/", views.boardgame_detail, name="boardgame_detail"),
]
