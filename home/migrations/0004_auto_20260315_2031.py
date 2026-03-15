from django.db import migrations


def create_genres(apps, schema_editor):
    Genre = apps.get_model('home', 'Genre')
    genre_names = [
        "Dungeon Crawler", "Roleplaying", "Cooperative", "Deck Builder",
        "Strategy", "Worker Placement", "Engine Builder", "Legacy",
        "Tile Laying", "Social Deduction", "Drafting", "Party", "4X",
        "Area Control", "Puzzle", "Miniature", "Travel", "Survival",
        "Roll and Write", "Adult", "Family"
    ]
    for name in genre_names:
        Genre.objects.create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_genre_id'),
    ]

    operations = [
        migrations.RunPython(create_genres),
    ]
