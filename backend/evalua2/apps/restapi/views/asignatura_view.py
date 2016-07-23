# -*- coding: utf-8 -*-

import unicodedata
from collections import OrderedDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Curso
from core.models import Asignatura
from core.models import CategoriaBloom
from core.models import CategoriaBloomValor
from core.models import ResultadoAprendizaje
from restapi.models import CursoSerializer
from restapi.models import AsignaturaSerializer
from restapi.models import ResultadoAprendizajeSerializer


from pprint import pprint


@api_view(['GET'])
def curso_list(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        data = []
        for c in serializer.data:
            serializer_vals = AsignaturaSerializer(Asignatura.objects.filter(curso_id=c['id']), many=True)
            c['values'] = sorted(serializer_vals.data, key=lambda k: k['name'])
            data.append(c)
        return Response(data)

@api_view(['GET'])
def curso(request, pk):
    try:
        curso = Curso.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursoSerializer(curso)
        data = serializer.data
        serializer_vals = AsignaturaSerializer(Asignatura.objects.filter(curso_id=data['id']), many=True)
        data['values'] = sorted(serializer_vals.data, key=lambda k: k['name'])
        return Response(data)


@api_view(['GET'])
def asignatura_list(request):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        serializer = AsignaturaSerializer(asignaturas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def asignatura(request, pk):
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AsignaturaSerializer(asignatura)
        data = serializer.data
        res = []
        for ra in ResultadoAprendizaje.objects.filter(asig_id=data['id']):
            vals = ResultadoAprendizajeSerializer(ra).data
            vals['analysis'] = analyze_ra(ra.name)
            res.append(vals)
        data['values'] = sorted(res, key=lambda k: k['name'])
        return Response(data)


def analyze_ra(ra_name):
    """
    Comparamos cada palabra del resultado de aprendizaje con todos los verbos
    de las categorías de bloom.
    """
    res = {
        'phrase': [],
        'categs': {c.name: 0 for c in CategoriaBloom.objects.all()}
    }

    # Quitamos acentos y pasamos a minusculas
    unaccent_categs = {unicodedata.normalize('NFKD', c).encode('ASCII', 'ignore').lower(): c for c in res['categs']}

    # Mientras no haya ningún token que pertenezca a alguna categoria de bloom
    # reconstruimos la frase en esta variable
    phrase = ''
    for token in ra_name.split(' '):
        unaccent_token = unicodedata.normalize('NFKD', token).encode('ASCII',
                                                                     'ignore').lower()  # Eliminamos los acentos
        cat_bloom = CategoriaBloomValor.objects.filter(name__iexact=token)
        if cat_bloom or unaccent_token in unaccent_categs.keys():
            # Guardamos la parte de la frase reconstruida hasta ahora
            if phrase:
                res['phrase'].append([phrase])
                phrase = ''
            tokens = [token]
            # Si el token actual coincide con algun verbo de bloom añadimos a la lista las categorias de los verbos
            # y añadimos un ocurrencia más al contador de categorias.
            if cat_bloom:
                for c in cat_bloom:
                    res['categs'][c.categ_id.name] += 1
                    tokens.append([c.categ_id.name])
            else:
                # Si el token es una de las categorias y no es un verbo
                tokens.append(token)
                res['categs'][unaccent_categs[unaccent_token]] += 1

            res['phrase'].append(tokens)
        else:
            phrase = '%s %s' % (phrase, token) if phrase else token
    if phrase:
        res['phrase'].append([phrase])

    return res