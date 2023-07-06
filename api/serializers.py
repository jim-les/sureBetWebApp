from rest_framework import serializers
from .models import Competition, Game, GameWinner, GameOverUnder15

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

        # fields = ['game_url']