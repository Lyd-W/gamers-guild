from django.shortcuts import render
from django.views import generic
from .models import Boardgame


class BoardgameList(generic.ListView):
    queryset = Boardgame.objects.all()
    context_object_name = "boardgames"
    template_name = "home/index.html"
    paginate_by = 6
