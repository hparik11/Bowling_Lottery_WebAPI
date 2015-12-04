# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jackpot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='bowler',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bowler',
            name='password',
        ),
        migrations.AddField(
            model_name='bowler',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 9, 1, 4, 349418, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bowler',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AddField(
            model_name='league',
            name='bowler',
            field=models.ForeignKey(related_name='bowler_id', to='jackpot.Bowler'),
        ),
    ]
