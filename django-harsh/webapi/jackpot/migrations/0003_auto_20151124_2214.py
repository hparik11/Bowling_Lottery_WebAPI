# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackpot', '0002_auto_20151124_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='bowler',
            field=models.IntegerField(),
        ),
    ]
