from rest_framework import serializers
from .models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            'name',
            'league',
            'points',
            'players'

        )


class MiniTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name',

        )


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'points']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class MiniGameSerializer(serializers.ModelSerializer):
    team_1 = TeamSerializer()
    team_2 = TeamSerializer()

    class Meta:
        model = Game
        fields = (
            'id',
            'team_1',
            'team_2',
            'team_1_score',
            'team_2_score',

        )

    def create(self, validated_data):
        game = Game.objects.create(**validated_data)
        return game
