# -*- coding: utf-8 -*-

from rest_framework import serializers
from core.models import ResultadoAprendizaje


class ResultadoAprendizajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizaje