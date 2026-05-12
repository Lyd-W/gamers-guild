from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Boardgame, Review


@admin.register(Boardgame)
class BoardgameAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'release_year',
                    'min_players', 'max_players')
    list_filter = ('genres', 'release_year')
    search_fields = ('title', 'description', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    filter_horizontal = ('genres',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('boardgame', 'user', 'rating', 'is_approved', 'created_on')
    list_filter = ('is_approved', 'created_on')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
