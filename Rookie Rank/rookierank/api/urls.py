from django.urls import path
from .views import CreateRankRoomView, RankRoomView

urlpatterns = [
    path('rankroom', RankRoomView.as_view()),
    path('create-rankroom', CreateRankRoomView.as_view())
]
