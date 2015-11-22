# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NFC_PW', models.CharField(max_length=35)),
                ('IO', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
