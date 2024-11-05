from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializerMovie import *


@api_view(['GET'])
def directors_list(request):
    directors = Director.objects.all()
    data = Serializer(instance=directors, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    data = Serializer2(instance=movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    data = Serializer3(instance=review, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail_review_list(request, id):
    try:
        review = Review.objects.get(id=id)
        data = Serializer3(review, many=False).data
        return Response(data=data)
    except Exception as e:
        return Response("this id doesnt exist")


@api_view(['GET'])
def detail_movie_list(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = Serializer2(movie, many=False).data
        return Response(data=data)
    except Exception as e:
        return Response("this id doesnt exist")


@api_view(['GET'])
def detail_director_list(request, id):
    try:
        director = Director.objects.get(id=id)
        data = Serializer(director, many=False).data
        return Response(data=data)
    except Exception as e:
        return Response("this id doesnt exist")
