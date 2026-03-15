from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

GENRE_TYPES = (
    (1, "Dungeon Crawler"),
    (2, "Roleplaying"),
    (3, "Cooperative"),
    (4, "Deck Builder"),
    (5, "Strategy"),
    (6, "Worker Placement"),
    (7, "Engine Builder"),
    (8, "Legacy"),
    (9, "Tile Laying"),
    (10, "Social Deduction"),
    (11, "Drafting"),
    (12, "Party"),
    (13, "4X"),
    (14, "Area Control"),
    (15, "Puzzle"),
    (16, "Miniature"),
    (17, "Travel"),
    (18, "Survival"),
    (19, "Roll and Write"),
    (20, "Adult"),

)
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Boardgame(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="boardgame"
    )
    created_on = models.DateField(auto_now_add=True)
    description = models.TextField()
    release_year = models.PositiveIntegerField(validators=[
        MinValueValidator(1940),
        MaxValueValidator(2100)
    ])
    playtime = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])
    genres = models.ManyToManyField(Genre, related_name='boardgames')
    min_players = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
        ])
    max_players = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.min_players > self.max_players:
            raise ValidationError({
                'min_players': ('Minimum number of players must be less than '
                                'or equal to maximum number of players.')
            })
