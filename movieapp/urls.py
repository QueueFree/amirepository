from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetailAPIView.as_view()),

]
