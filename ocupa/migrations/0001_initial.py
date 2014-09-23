# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.BooleanField(default=True)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(upload_to=b'ocupa')),
                ('outro', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Quest\xe3o',
                'verbose_name_plural': 'Quest\xf5es',
            },
            bases=(models.Model,),
        ),
    ]
