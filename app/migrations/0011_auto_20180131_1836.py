# Generated by Django 2.0 on 2018-01-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180131_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrocinador',
            name='pequeno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='tipo',
            field=models.IntegerField(),
        ),
    ]
