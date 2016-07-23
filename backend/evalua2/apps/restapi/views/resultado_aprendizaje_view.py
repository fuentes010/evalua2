# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import ResultadoAprendizaje
from restapi.models import ResultadoAprendizajeSerializer
from restapi.views import analyze_ra


@api_view(['GET'])
def resultado_aprendizaje_list(request):
    if request.method == 'GET':
        categorias = ResultadoAprendizaje.objects.all()
        serializer = ResultadoAprendizajeSerializer(categorias, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def resultado_aprendizaje(request, pk):
    try:
        categoria = ResultadoAprendizaje.objects.get(pk=pk)
    except ResultadoAprendizaje.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResultadoAprendizajeSerializer(categoria)
        return Response(serializer.data)


@api_view(['POST'])
def analizar_resultado_aprendizaje(request):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if request.method == 'POST':
        res = []
        for ra in request.data:
            res.append({'name': ra,
                        'analysis': analyze_ra(ra['name'])})

        return Response(sorted(res, key=lambda k: k['name']))