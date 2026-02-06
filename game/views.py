from re import search
from urllib import request
from django.shortcuts import render, get_object_or_404


import game
from .models import Game, Studio, Platform, Categories
from django.db.models import Q

def home(request):
    games = Game.objects.all()[:6]
    return render(request, 'game/home.html', {'games': games})

def about(request):
    return render(request, 'game/about.html', {})
    
def game_list(request):
    games = Game.objects.all()
    search = request.GET.get('search', '')
    
    if search:
        games = games.filter(title__icontains=search)
    category_id = request.GET.get('category', '')
    
    if category_id:
        games = games.filter(categories__id=category_id)
    platform_id = request.GET.get('platform', '')
    
    if platform_id:
        games = games.filter(platform__id=platform_id) 
    
    sort = request.GET.get('sort', '')
    
    if sort == 'title_asc':
        games = games.order_by('title')
    elif sort == 'title_desc':
        games = games.order_by('-title')
    elif sort == 'rating_asc':
        games = games.order_by('metacritic_score')
    elif sort == 'rating_desc':
        games = games.order_by('-metacritic_score')
    elif sort == 'release_date_asc':
        games = games.order_by('release_date')
    elif sort == 'release_date_desc':
        games = games.order_by('-release_date')
    
    games = games.distinct()

    categories = Categories.objects.all()
    platforms = Platform.objects.all()

    return render(request, 'game/game_list.html', {
    'games': games,
    'categories': categories,
    'platforms': platforms,})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game/game_detail.html', {'game': game})

