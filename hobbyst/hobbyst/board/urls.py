from django.urls import path
from board.views import home

urlpatterns = [
    path('', home),
]