# Generated by Django 4.1.4 on 2022-12-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('contenido', models.CharField(max_length=600)),
                ('imgenes', models.URLField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
