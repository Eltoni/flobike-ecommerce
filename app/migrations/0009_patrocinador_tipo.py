# Generated by Django 2.0 on 2018-01-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_patrocinador'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrocinador',
            name='tipo',
            field=models.IntegerField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
