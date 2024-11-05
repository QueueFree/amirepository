from rest_framework import serializers
from .models import *


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class Serializer2(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class Serializer3(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
