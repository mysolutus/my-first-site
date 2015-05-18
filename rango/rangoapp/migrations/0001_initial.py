# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='rangoapp.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
