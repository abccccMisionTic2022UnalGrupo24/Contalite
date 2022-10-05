# Generated by Django 4.1 on 2022-10-04 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empresas', '0002_alter_empresa_nit'),
        ('Transacciones', '0002_alter_transaccion_concepto'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='id_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Empresas.empresa'),
        ),
    ]