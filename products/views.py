from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializer import ProductSerializer


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    data = ProductSerializer(instance=products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def test(request):
    dicte = {
        'test': 'test'
    }
    return Response(data=dicte, status=status.HTTP_200_OK)