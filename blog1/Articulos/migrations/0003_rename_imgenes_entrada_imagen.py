# Generated by Django 4.1.4 on 2022-12-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0002_alter_entrada_contenido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='imgenes',
            new_name='imagen',
        ),
    ]
