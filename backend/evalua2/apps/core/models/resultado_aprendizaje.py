# -*- coding: utf-8 -*-

from django.db import models


class ResultadoAprendizaje(models.Model):

    name = models.CharField('Nombre', max_length=200)

