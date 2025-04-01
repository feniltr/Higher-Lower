from rest_framework import viewsets
from .models import Game, Category
from .serializers import GameSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import random
from rest_framework.views import APIView
from rest_framework import status

class RandomGamesAPIView(APIView):
    def get(self, request, format=None):
        games = list(Game.objects.all())
        if len(games) < 2:
            return Response({"error": "Not enough games available"}, status=status.HTTP_400_BAD_REQUEST)
        
        random_games = random.sample(games, 2)
        serializer = GameSerializer(random_games, many=True)
        data = {
            'leftItem': serializer.data[0],
            'rightItem': serializer.data[1]
        }
        return Response(data)

class SingleRandomGameAPIView(APIView):
    def get(self, request, format=None):
        games = list(Game.objects.all())
        if not games:
            return Response({"error": "No games available"}, status=status.HTTP_400_BAD_REQUEST)
        
        random_game = random.choice(games)
        serializer = GameSerializer(random_game)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
