# Generated by Django 5.0.3 on 2024-03-06 03:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computacion_api', '0004_maestro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alummos',
            new_name='Alumnos',
        ),
    ]
