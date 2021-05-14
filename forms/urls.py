from django.urls import path

from . import views

urlpatterns = [
    path('', views.RGAform, name='RGA cart tracking form'),
    path('history/', views.History, name='History'),
]
