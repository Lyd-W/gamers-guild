from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Boardgame

# Register your models here.

@admin.register(Boardgame)
class BoardgameAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'release_year', 'genre', 'rating', 
                    'min_players', 'max_players')
    list_filter = ('genre', 'release_year', 'rating')
    search_fields = ('title', 'description', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')