# Generated by Django 4.1 on 2022-09-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiorTransaccional', '0011_remove_user_rol_user_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id_empleado',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id_tr',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
