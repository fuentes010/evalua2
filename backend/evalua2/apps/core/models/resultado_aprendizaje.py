# -*- coding: utf-8 -*-
from django.db import models
from core.models import Asignatura

class ResultadoAprendizaje(models.Model):

    name = models.CharField('Nombre', max_length=200)
    asig_id = models.ForeignKey(Asignatura)


