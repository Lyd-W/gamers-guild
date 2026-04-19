from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("<slug:slug>/", views.boardgame_detail, name="boardgame_detail"),
]
