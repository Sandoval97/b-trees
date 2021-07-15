
from django.contrib import admin
from django.urls import path
from .views import height, neighbors, bfs

app_name = "btree"

urlpatterns = [
    path('height/', height, name="height"),
    path('neighbors/', neighbors, name="neighbors"),
    path('bfs/', bfs, name="bfs"),
]
