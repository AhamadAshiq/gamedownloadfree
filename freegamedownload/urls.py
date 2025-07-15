from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_games, name='search'),
    path('android/', views.android_games, name='android_games'),
    path('ios/', views.ios_games, name='ios_games'),
    path('pc/', views.pc_games, name='pc_games'),
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)