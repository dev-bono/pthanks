# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thanks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user_id', models.IntegerField(max_length=11)),
                ('thanks_to', models.IntegerField(max_length=11)),
                ('memo', models.TextField(max_length=500)),
                ('create_dt', models.DateTimeField()),
                ('heart_count', models.IntegerField()),
                ('thanks_type', models.CharField(max_length=1)),
            ],
        ),
    ]
