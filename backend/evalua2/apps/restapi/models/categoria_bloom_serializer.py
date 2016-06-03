# -*- coding: utf-8 -*-

from rest_framework import serializers
from core.models import CategoriaBloom, CategoriaBloomValor


class CategoriaBloomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaBloom


class CategoriaBloomValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaBloomValor