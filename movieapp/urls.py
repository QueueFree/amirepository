from django.urls import path
from . import views

urlpatterns = [
    path('', views.directors_list),
    path('<int:id>/', views.detail_director_list),
]
