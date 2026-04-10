from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Boardgame, Genre


def home(request):
    boardgames = Boardgame.objects.all()
    genres = Genre.objects.all()

    query = None
    selected_genres = []
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            boardgames = boardgames.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

    if 'genre' in request.GET:
        selected_genres = request.GET.getlist('genre')
        if selected_genres:
            boardgames = boardgames.filter(
                genres__id__in=selected_genres
            ).distinct()

    if 'sort' in request.GET:
        sort = request.GET.get('sort')
        direction = request.GET.get('direction')

        if sort == 'title':
            boardgames = boardgames.annotate(
                lower_title=Lower('title')
            )
            sortkey = 'lower_title'
        elif sort == 'playtime':
            sortkey = 'playtime'
        elif sort == 'release_year':
            sortkey = 'release_year'
        else:
            sortkey = sort

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        boardgames = boardgames.order_by(sortkey)

    current_sorting = f"{sort}_{direction}"

    min_players = request.GET.get('min_players')
    max_players = request.GET.get('max_players')

    if min_players:
        boardgames = boardgames.filter(min_players__lte=min_players)

    if max_players:
        boardgames = boardgames.filter(max_players__gte=max_players)
        
    playtime = request.GET.get('playtime')

    if playtime:
        boardgames = boardgames.filter(playtime__lte=playtime)

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
