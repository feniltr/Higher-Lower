from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RandomGamesAPIView, CategoryViewSet, SingleRandomGameAPIView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('random-games/', RandomGamesAPIView.as_view(), name='random-games'),
    path('random-games/single/', SingleRandomGameAPIView.as_view(), name='random-game-single'),
    path('', include(router.urls)),
]