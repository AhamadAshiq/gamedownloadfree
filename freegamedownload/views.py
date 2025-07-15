from django.shortcuts import render, get_object_or_404
from .models import Game
from .models import FeaturedGame


from django.db.models import Q

def search_games(request):
    query = request.GET.get('q')
    games = []

    if query:
        games = Game.objects.filter(
            Q(title__icontains=query) |
            Q(platform__icontains=query)
        )

    return render(request, 'search_results.html', {'games': games, 'query': query})

def home(request):
    featured_games = FeaturedGame.objects.all()
    games = Game.objects.all()[:6]
    return render(request, 'index.html', {
        'featured_games': featured_games,
        'games': games
    })

def android_games(request):
    games = Game.objects.filter(platform='android')
    return render(request, 'android.html', {'games': games})

def ios_games(request):
    games = Game.objects.filter(platform='ios')
    return render(request, 'ios.html', {'games': games})

def pc_games(request):
    games = Game.objects.filter(platform='pc')
    return render(request, 'pc.html', {'games': games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    related_games = Game.objects.filter(platform=game.platform).exclude(id=game.id)[:4]
    return render(request, 'game-details.html', {'game': game, 'related_games': related_games})



