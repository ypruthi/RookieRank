from rest_framework import serializers
from .models import RankRoom

class RankRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankRoom
        fields = ('id','name', 'host', 'number_of_players', 
        'choose_players','created_at')

class CreateRankRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankRoom
        fields = ('number_of_players', 'choose_players')
