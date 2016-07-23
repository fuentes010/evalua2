# -*- coding: utf-8 -*-

from django.db import models

class Curso(models.Model):

    name = models.CharField('Nombre', max_length=200)


class Asignatura(models.Model):

    name = models.CharField('Nombre', max_length=200)
    curso_id = models.ForeignKey(Curso)

