from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializerMovie import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


class DirectorListAPIView(ListCreateAPIView):
    serializer_class = Serializer
    queryset = Director.objects.all()
    pagination_class = CustomPagination


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Serializer
    queryset = Director.objects.all()
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# def directors_list(request):
#     print(request.user)
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = Serializer(instance=directors, many=True).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid()
#         if not serializer.is_valid():
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         name = serializer.validated_data.get('name')
#
#         new = Director.objects.create(
#             name=name
#         )
#         new.save()
#         return Response(status=status.HTTP_201_CREATED, data=Serializer(new).data)


class MovieListAPIView(ListCreateAPIView):
    serializer_class = Serializer2
    queryset = Movie.objects.all()
    pagination_class = CustomPagination


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Serializer2
    queryset = Movie.objects.all()
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     print(request.user)
#     if request.method == 'GET':
#         movies = Movie.objects.prefetch_related('reviews', 'director').all()
#         data = Serializer2(instance=movies, many=True).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid()
#         if not serializer.is_valid():
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director = serializer.validated_data.get('director')
#
#         new = Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director=director
#         )
#
#         new.director.set(director)
#         new.save()
#         return Response(status=status.HTTP_201_CREATED, data=Serializer2(new).data)


class ReviewListAPIView(ListCreateAPIView):
    serializer_class = Serializer3
    queryset = Review.objects.all()
    pagination_class = CustomPagination


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Serializer3
    queryset = Review.objects.all()
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         review = Review.objects.prefetch_related('movie').all()
#         data = Serializer3(instance=review, many=True).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid()
#         if not serializer.is_valid():
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         text = serializer.validated_data.get('text')
#         movie = serializer.validated_data.get('movie')
#         stars = serializer.validated_data.get('stars')
#
#         new = Review.objects.create(
#             text=text,
#             stars=stars
#         )
#         new.movie.set(movie)
#         new.save()
#         return Response(status=status.HTTP_201_CREATED, data=Serializer3(new).data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_review_list(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Exception as e:
#         return Response("this id doesnt exist")
#     if request.method == 'GET':
#         data = Serializer3(review, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         review.text = request.data.get('text')
#         review.stars = request.data.get('stars')
#         review.movie.set(request.data.get('movie'))
#         review.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data=Serializer3(review, many=False).data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_movie_list(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Exception as e:
#         return Response("this id doesnt exist")
#     if request.method == 'GET':
#         data = Serializer2(movie, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director.set(request.data.get('director'))
#         movie.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data=Serializer2(movie).data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_director_list(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Exception as e:
#         return Response("this id doesnt exist")
#     if request.method == 'GET':
#         data = Serializer(director, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         director.name = request.data.get('name')
#         director.save()
#         return Response(status=status.HTTP_201_CREATED, data=Serializer(director).data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
