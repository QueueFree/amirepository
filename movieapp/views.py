from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializerMovie import *


@api_view(['GET', 'POST'])
def directors_list(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = Serializer(instance=directors, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        new = Director.objects.create(
            name=name
        )
        new.save()
        return Response(status=status.HTTP_201_CREATED, data=Serializer(new).data)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.prefetch_related('reviews', 'director').all()
        data = Serializer2(instance=movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        new = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
        )

        new.director.set(director)
        new.save()
        return Response(status=status.HTTP_201_CREATED, data=Serializer2(new).data)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.prefetch_related('movie').all()
        data = Serializer3(instance=review, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        new = Review.objects.create(
            text=text,
            stars=stars
        )
        new.movie.set(movie)
        new.save()
        return Response(status=status.HTTP_201_CREATED, data=Serializer3(new).data)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_review_list(request, id):
    try:
        review = Review.objects.get(id=id)
    except Exception as e:
        return Response("this id doesnt exist")
    if request.method == 'GET':
        data = Serializer3(review, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie.set(request.data.get('movie'))
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=Serializer3(review, many=False).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_movie_list(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Exception as e:
        return Response("this id doesnt exist")
    if request.method == 'GET':
        data = Serializer2(movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director.set(request.data.get('director'))
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=Serializer2(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_director_list(request, id):
    try:
        director = Director.objects.get(id=id)
    except Exception as e:
        return Response("this id doesnt exist")
    if request.method == 'GET':
        data = Serializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(status=status.HTTP_201_CREATED, data=Serializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
