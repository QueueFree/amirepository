from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('login/', views.auth),
]
