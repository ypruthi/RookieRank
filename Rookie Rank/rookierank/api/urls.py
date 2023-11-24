from django.urls import path
from .views import PlayerView

urlpatterns = [
    path('player', PlayerView.as_view())
]
