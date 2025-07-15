from django.contrib import admin
from .models import Game, GameScreenshot

class ScreenshotInline(admin.TabularInline):
    model = GameScreenshot
    extra = 1

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ScreenshotInline]

admin.site.register(Game, GameAdmin)

    
from django.contrib import admin
from .models import FeaturedGame

admin.site.register(FeaturedGame)
