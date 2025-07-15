from django.db import models

PLATFORM_CHOICES = [
    ('android', 'Android'),
    ('ios', 'iOS'),
    ('pc', 'PC'),
]

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    platform = models.CharField(max_length=50, choices=[('android', 'Android'), ('ios', 'iOS'), ('pc', 'PC')])
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/')
    download_link = models.URLField()
    downloads = models.IntegerField(default=0)
    youtube_trailer = models.URLField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.title

class GameScreenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='game_screenshots/')


from django.db import models

class FeaturedGame(models.Model):
    title = models.CharField(max_length=200)
    label = models.CharField(max_length=50, default="Adventure")  # like: Action, Racing, etc.
    description = models.TextField()
    image = models.ImageField(upload_to='hero_images/')
    download_link = models.URLField()

    def __str__(self):
        return self.title
