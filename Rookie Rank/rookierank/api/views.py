from django.shortcuts import render
from rest_framework import generics
from .serializers import PlayerSerializer
from .models import Player

# Create your views here.
class PlayerView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

