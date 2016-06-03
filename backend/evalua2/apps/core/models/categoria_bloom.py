# -*- coding: utf-8 -*-

from django.db import models


class CategoriaBloom(models.Model):

    name = models.CharField('Nombre', max_length=200)
    seq = models.IntegerField('Secuencia')

    class Meta:
        verbose_name = "Categoria Bloom"
        verbose_name_plural = "Categorias Bloom"

    def __unicode__(self):
        return self.name


class CategoriaBloomRevisada(models.Model):

    name = models.CharField('Nombre', max_length=200)
    seq = models.IntegerField('Secuencia')

    class Meta:
        verbose_name = "Categoria Bloom revisado"
        verbose_name_plural = "Categorias Bloom revisado"

    def __unicode__(self):
        return self.name


class CategoriaBloomValor(models.Model):

    name = models.CharField('Nombre', max_length=200)
    categ_id = models.ForeignKey(CategoriaBloom)

    class Meta:
        verbose_name = "Valor categoria Bloom"
        verbose_name_plural = "Valores categorias Bloom"

    def __unicode__(self):
        return self.name
