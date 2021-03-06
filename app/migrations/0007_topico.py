# Generated by Django 2.0 on 2018-01-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180129_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=15)),
                ('data_add', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(help_text='Preenchido automaticamente, não editar.', max_length=255, unique=True, verbose_name='Slug / URL')),
            ],
        ),
    ]
