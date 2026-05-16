from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg
from django.db.models.functions import Lower, Coalesce
from django.db.models import FloatField
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied



from .models import Boardgame, Genre, Review
from .forms import ReviewForm
from django.contrib import messages
from shop.models import Product


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
        
    player_options = [1, 2, 3, 4, 5, 6]
    selected_players = request.GET.getlist("players")

    selected_players = request.GET.getlist("players")

    if selected_players:
        q = Q()

        for p in selected_players:
            p = int(p)
            q |= Q(min_players__lte=p, max_players__gte=p)

        boardgames = boardgames.filter(q)

    if playtime:
        boardgames = boardgames.filter(playtime__lte=playtime)

    sortkey = "title"

    boardgames = boardgames.annotate(
        avg_rating=Coalesce(
            Avg(
                'reviews__rating',
                filter=Q(reviews__is_approved=True)
            ),
            0.0,
            output_field=FloatField()
        )
    )
    sortkey = "title"

    if sort == "rating":
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
        'player_options': player_options,
        'current_players': selected_players,
    }

    return render(request, "home/index.html", context)


def boardgame_detail(request, slug):
    boardgame = get_object_or_404(
        Boardgame.objects.annotate(
            avg_rating=Coalesce(
                Avg(
                    'reviews__rating',
                    filter=Q(reviews__is_approved=True)
                ),
                0.0,
                output_field=FloatField()
            )
        ),
        slug=slug
    )

    reviews = []

    review = None
    if request.user.is_authenticated:
        review = Review.objects.filter(
            boardgame=boardgame,
            user=request.user
        ).first()

    if request.user.is_staff:
        reviews = boardgame.reviews.all().order_by('-created_on')

    elif request.user.is_authenticated:
        reviews = boardgame.reviews.filter(
            Q(is_approved=True) | Q(user=request.user)
        ).order_by('-created_on')

    else:
        reviews = boardgame.reviews.filter(
            is_approved=True
        ).order_by('-created_on')

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "You must be logged in to leave a review.")
            return redirect('boardgame_detail', slug=boardgame.slug)

    review_id = request.POST.get("review_id")

    if review_id:
        review = Review.objects.get(id=review_id, boardgame=boardgame)

    form = ReviewForm(request.POST, instance=review)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.boardgame = boardgame
        new_review.user = request.user
        new_review.is_approved = False
        new_review.save()

        messages.success(request, "Review submitted!")
        return redirect('boardgame_detail', slug=boardgame.slug)

    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "home/boardgame_detail.html",
        {
            "boardgame": boardgame,
            "form": form,
            "reviews": reviews,
        }
    )


@login_required
def delete_review(request, slug, review_id):
    boardgame = get_object_or_404(Boardgame, slug=slug)
    review = get_object_or_404(Review, id=review_id, boardgame=boardgame)

    if review.user != request.user and not request.user.is_staff:
        messages.warning(request, "You cannot delete this review.")
        return redirect('boardgame_detail', slug=slug)

    review.delete()
    messages.success(request, "Review deleted.")
    return redirect('boardgame_detail', slug=slug)


@login_required
def toggle_favourite(request, slug):
    boardgame = get_object_or_404(Boardgame, slug=slug)

    if request.user in boardgame.favourites.all():
        boardgame.favourites.remove(request.user)
        messages.success(request, "Removed from favourites.")
    else:
        boardgame.favourites.add(request.user)
        messages.success(request, "Added to favourites.")

    return redirect('boardgame_detail', slug=slug)


def search(request):
    query = request.GET.get('q')

    boardgames = Boardgame.objects.all()
    products = Product.objects.all()

    if query:
        boardgames = boardgames.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        boardgames = Boardgame.objects.none()
        products = Product.objects.none()

    context = {
        "query": query,
        "boardgames": boardgames,
        "products": products,
    }

    return render(request, "home/search/results.html", context)


@login_required
def approve_review(request, review_id):
    if not request.user.is_staff:
        return redirect('home')

    review = get_object_or_404(Review, id=review_id)
    review.is_approved = True
    review.save()

    return redirect(request.META.get('HTTP_REFERER'))


def custom_400(request, exception):
    return render(request, "errors/400.html", status=400)


def custom_403(request, exception):
    return render(request, "errors/403.html", status=403)


def custom_500(request):
    return render(request, "errors/500.html", status=500)


def trigger_400(request):
    return HttpResponseBadRequest("Test 400 Error")


def trigger_403(request):
    raise PermissionDenied


def trigger_500(request):
    raise Exception("Test 500 Error")