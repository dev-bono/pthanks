# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thanks',
            name='thanks_to',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thanks',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
