# Generated by Django 4.1.4 on 2023-01-03 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compraEnCafa', '0005_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]