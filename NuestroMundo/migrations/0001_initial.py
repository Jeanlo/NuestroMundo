# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('codigo_pais', models.CharField(max_length=3)),
                ('distrito', models.CharField(max_length=60)),
                ('poblacion', models.IntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma_Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('codigo_pais', models.CharField(max_length=3)),
                ('idioma', models.CharField(max_length=40)),
                ('porcentaje', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=60)),
                ('continente', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=40)),
                ('area', models.DecimalField(max_digits=22, decimal_places=2)),
                ('independencia', models.IntegerField(default=1948)),
                ('poblacion', models.IntegerField(default=1000000)),
                ('esperanza_vida', models.DecimalField(max_digits=3, decimal_places=1)),
                ('PIB', models.DecimalField(max_digits=18, decimal_places=2)),
                ('PIB_anterior', models.DecimalField(max_digits=18, decimal_places=2)),
                ('nombre_local', models.CharField(max_length=60)),
                ('tipo_gobierno', models.CharField(max_length=80)),
                ('lider_estado', models.CharField(max_length=60)),
                ('capital', models.IntegerField()),
                ('codigo_corto', models.CharField(max_length=2)),
            ],
        ),
    ]
