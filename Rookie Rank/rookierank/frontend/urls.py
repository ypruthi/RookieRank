from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('rankroom', index),
    path('create', index),
    path('room/<str:roomName>', index)
]