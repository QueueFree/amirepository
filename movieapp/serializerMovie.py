from rest_framework import serializers
from rest_framework.fields import ListField

from .models import *


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies'.split()


class Serializer2(serializers.ModelSerializer):
    director = Serializer()

    class Meta:
        model = Movie
        fields = 'title description duration reviews director'.split()
        depth = 1


class Serializer3(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars rating movie'.split()


class DirRevSerializer(serializers.ModelSerializer):
    class Meta:
        director = Serializer(many=True)
        review = Serializer3(many=True)


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=39)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=80)
    description = serializers.CharField(max_length=5000)
    duration = serializers.CharField()
    director = ListField(child=serializers.IntegerField())


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie = ListField(child=serializers.IntegerField())
