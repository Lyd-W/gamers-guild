from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Boardgame(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(
        upload_to='boardgames/',
        null=True,
        blank=True
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


class Review(models.Model):
    boardgame = models.ForeignKey(
        Boardgame,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('boardgame', 'user')

    def __str__(self):
        return f"{self.boardgame.title} - {self.rating}"
