# Generated by Django 4.1 on 2023-10-23 09:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
    ]