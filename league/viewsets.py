from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from .models import *


# Create your views here.


class PlayersViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class LeagueViewset(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TableSerializer

class GameViewset(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CreateGameViewSet(viewsets.ModelViewSet):
    serializer_class = MiniGameSerializer
    queryset = Game.objects.all()
