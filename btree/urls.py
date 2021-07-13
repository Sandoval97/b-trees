
from django.contrib import admin
from django.urls import path
from .views import height, neighbors, bfs

app_name = "btree"

urlpatterns = [
    path('height/', height),
    path('neighbors/', neighbors),
    path('bfs/', bfs),
]
