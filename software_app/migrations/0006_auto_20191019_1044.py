# Generated by Django 2.2.6 on 2019-10-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_app', '0005_auto_20191019_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcion',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
