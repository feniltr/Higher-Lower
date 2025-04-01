# game/admin.py

from django.contrib import admin
from .models import Game, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'num_searches', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('tag_name',)
