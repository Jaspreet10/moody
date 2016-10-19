# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('compound', models.DecimalField(max_digits=19, decimal_places=10)),
                ('neg', models.DecimalField(max_digits=19, decimal_places=10)),
                ('neu', models.DecimalField(max_digits=19, decimal_places=10)),
                ('pos', models.DecimalField(max_digits=19, decimal_places=10)),
            ],
        ),
    ]
