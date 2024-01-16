from django.contrib import admin
from django.urls import path, include
from .views import HomeView, trips_list


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trips-list'),
]
