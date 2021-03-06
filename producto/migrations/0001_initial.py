# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-26 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25, unique=True, verbose_name='C\xf3digo')),
                ('producto', models.CharField(max_length=45, unique=True, verbose_name='Producto')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripci\xf3n')),
                ('cantidad', models.PositiveSmallIntegerField(verbose_name='cantidad')),
                ('valorIva', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='IVA')),
                ('valorVenta', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Valor de venta')),
            ],
        ),
    ]
