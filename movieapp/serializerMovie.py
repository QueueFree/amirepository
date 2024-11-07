from rest_framework import serializers
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
