# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jackpot', '0004_auto_20151124_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('bowler_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='bowler',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
