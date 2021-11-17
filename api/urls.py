"""
    API URLS
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from league.viewsets import *

router = DefaultRouter()
router.register(r'league', LeagueViewset)
router.register(r'team', TeamViewset)
router.register(r'player', PlayersViewset)
router.register(r'game', GameViewset)



urlpatterns = [
    path('admin/', admin.site.urls),

    # for the browserble API
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(router.urls)),
    # Start a league /league/start (POST)
    path('games/create', CreateGameViewSet.as_view({'post': 'create'}), name='create_game'),
    # Create a Team /teams/create (POST)
    path('table/', TableViewSet.as_view({'get': 'list'}), name='table'),
]
