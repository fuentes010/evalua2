# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160510_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaBloomRevisada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('seq', models.IntegerField(verbose_name=b'Secuencia')),
            ],
            options={
                'verbose_name': 'Categoria Bloom revisado',
                'verbose_name_plural': 'Categorias Bloom revisado',
            },
        ),
    ]