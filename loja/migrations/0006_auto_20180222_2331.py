# Generated by Django 2.0 on 2018-02-22 23:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_auto_20180212_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
