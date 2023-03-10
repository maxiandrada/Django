# Generated by Django 4.1.4 on 2023-01-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compraEnCafa', '0006_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagePortada',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_choice',
            field=models.CharField(blank=True, choices=[('Cliente', 'Quiero comprar'), ('Comerciante', 'Quiero vender')], default='d', help_text='Seccion de Noticia', max_length=50),
        ),
    ]
