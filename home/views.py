from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from django.db.models.functions import Lower, Coalesce
from django.db.models import FloatField

from .models import Boardgame, Genre


def home(request):
    boardgames = Boardgame.objects.all()
    genres = Genre.objects.all()

    query = request.GET.get('q')
    selected_genres = request.GET.getlist('genre')

    sort = request.GET.get('sort')
    direction = request.GET.get('direction', 'asc')

    min_players = request.GET.get('min_players')
    max_players = request.GET.get('max_players')
    playtime = request.GET.get('playtime')

    if query:
        boardgames = boardgames.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if selected_genres:
        boardgames = boardgames.filter(
            genres__id__in=selected_genres
        ).distinct()

    if min_players:
        boardgames = boardgames.filter(min_players__lte=min_players)

    if max_players:
        boardgames = boardgames.filter(max_players__gte=max_players)

    if playtime:
        boardgames = boardgames.filter(playtime__lte=playtime)

    sortkey = "title"

    if sort == "rating":
        boardgames = boardgames.annotate(
            avg_rating=Coalesce(
                Avg('reviews__rating'),
                0.0,
                output_field=FloatField()
            )
        )
        sortkey = "avg_rating"

    elif sort == "title":
        boardgames = boardgames.annotate(
            lower_title=Lower('title')
        )
        sortkey = "lower_title"

    elif sort == "playtime":
        sortkey = "playtime"

    elif sort == "release_year":
        sortkey = "release_year"

    if direction == "desc":
        sortkey = f"-{sortkey}"

    boardgames = boardgames.order_by(sortkey)

    current_sorting = f"{sort}_{direction}" if sort else "None_None"

    context = {
        'boardgames': boardgames,
        'genres': genres,
        'search_term': query,
        'current_genres': selected_genres,
        'current_sorting': current_sorting,
    }

    return render(request, "home/index.html", context)


def boardgame_detail(request, slug):
    boardgame = get_object_or_404(Boardgame, slug=slug)

    return render(
        request,
        "home/boardgame_detail.html",
        {"boardgame": boardgame}
    )
