from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RankRoomSerializer, CreateRankRoomSerializer
from .models import RankRoom
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RankRoomView(generics.ListAPIView):
    queryset = RankRoom.objects.all()
    serializer_class = RankRoomSerializer

class CreateRankRoomView(APIView):
    serializer_class = CreateRankRoomSerializer


    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            number_of_players = serializer.data.get('number_of_players')
            choose_players = serializer.data.get('choose_players')
            host = self.request.session.session_key
            queryset = RankRoom.objects.filter(host=host)
            if queryset.exists():
                rankroom = queryset[0]
                rankroom.number_of_players = number_of_players
                rankroom.choose_players = serializer.data.get('choose_players')
                rankroom.save(update_fields=['number_of_players', 'choose_players'])
                return Response(RankRoomSerializer(rankroom).data, status=status.HTTP_200_OK)
            else:
                rankroom = RankRoom(host=host, number_of_players = number_of_players,
                                    choose_players = choose_players)
                rankroom.save()
                return Response(RankRoomSerializer(rankroom).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)