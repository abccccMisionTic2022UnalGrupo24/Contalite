# Generated by Django 4.1 on 2022-10-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transacciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='concepto',
            field=models.TextField(max_length=1000, verbose_name='Concepto'),
        ),
    ]
