# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import CategoriaBloom, CategoriaBloomValor
from restapi.models import CategoriaBloomSerializer, CategoriaBloomValorSerializer


@api_view(['GET'])
def categorias_bloom_list(request):
    if request.method == 'GET':
        categorias = CategoriaBloom.objects.all()
        serializer = CategoriaBloomSerializer(categorias, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def categorias_bloom(request, pk):
    try:
        categoria = CategoriaBloom.objects.get(pk=pk)
    except CategoriaBloom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaBloomSerializer(categoria)
        return Response(serializer.data)


@api_view(['GET'])
def categorias_bloom_valor_list(request):
    if request.method == 'GET':
        categorias = CategoriaBloomValor.objects.all()
        serializer = CategoriaBloomValorSerializer(categorias, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def categorias_bloom_valor(request, pk):
    try:
        categoria = CategoriaBloomValor.objects.get(pk=pk)
    except CategoriaBloomValor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaBloomValorSerializer(categoria)
        return Response(serializer.data)