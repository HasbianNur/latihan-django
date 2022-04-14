from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buku/', views.buku),
    path('user/', views.user),
    path('komentar/', views.komentar)
]
