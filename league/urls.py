"""
    APP URLS
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register(r'league', LeagueViewset)
router.register(r'team', TeamViewset)
router.register(r'player', PlayersViewset)
router.register(r'game', GameViewset)


urlpatterns = [
    # Start a league /league/start (POST)

    # Create a Team /teams/create (POST)
    # Add a Player to a Team (Constraint: 11 Players) /team_id/players/add (POST)
    # Start a Game /game/start/team_1/team_2 (POST)
    # Record Scores /game_id/team_1_score/team_2_score (POST)
    # History of all the gmaes played /games (GET)
]
