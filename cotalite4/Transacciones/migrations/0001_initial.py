# Generated by Django 4.1 on 2022-09-29 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_tr', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], default='Elija una opcion', max_length=20, verbose_name='tipo')),
                ('fecha_tr', models.DateField(auto_now=True)),
                ('concepto', models.TextField(max_length=500, verbose_name='Concepto')),
                ('monto', models.IntegerField(verbose_name='Monto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaccion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]