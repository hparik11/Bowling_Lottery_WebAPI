# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bowler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('created', models.DateTimeField(verbose_name=b'date published')),
                ('password', models.CharField(max_length=6)),
                ('amount', models.IntegerField(default=1000)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
