# Generated by Django 4.1.4 on 2022-12-20 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_idioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.idioma'),
        ),
    ]
