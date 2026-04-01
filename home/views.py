from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Boardgame


class BoardgameList(generic.ListView):
    queryset = Boardgame.objects.all()
    context_object_name = "boardgames"
    template_name = "home/index.html"


def boardgame_detail(request, slug):
    boardgame = get_object_or_404(Boardgame, slug=slug)

    return render(
        request,
        "home/boardgame_detail.html",
        {"boardgame": boardgame}
    )
