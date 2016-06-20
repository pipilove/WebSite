# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(verbose_name='e-mail', blank=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(blank=True, max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(blank=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
