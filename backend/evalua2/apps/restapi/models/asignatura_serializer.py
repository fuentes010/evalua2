# -*- coding: utf-8 -*-

from rest_framework import serializers
from core.models import Curso
from core.models import Asignatura

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura

