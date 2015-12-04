# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jackpot', '0003_auto_20151124_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='bowler',
        ),
        migrations.AddField(
            model_name='league',
            name='bowler_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bowler',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
