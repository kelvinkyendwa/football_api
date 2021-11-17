from django.contrib import admin
from .models import *


# Register your models here.

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'league', 'points')


class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'team_1', 'team_2', 'team_1_score', 'team_2_score', 'winner', 'result')


admin.site.register(League, LeagueAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
