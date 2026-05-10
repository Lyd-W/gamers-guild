from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("search/", views.search, name="search"),
    path("<slug:slug>/favourite/", views.toggle_favourite, 
         name="toggle_favourite"),
    path("<slug:slug>/", views.boardgame_detail, name="boardgame_detail"),
    path("<slug:slug>/delete_review/<int:review_id>/", views.delete_review, name="delete_review"),
    path("review/<int:review_id>/approve/", views.approve_review, name="approve_review"),
    path("review/<int:review_id>/unapprove/", views.unapprove_review, name="unapprove_review"),
]
