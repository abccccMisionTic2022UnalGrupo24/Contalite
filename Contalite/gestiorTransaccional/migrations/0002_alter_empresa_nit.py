# Generated by Django 4.1 on 2022-09-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiorTransaccional', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]