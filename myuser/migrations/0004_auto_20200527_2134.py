# Generated by Django 3.0.6 on 2020-05-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0003_auto_20200527_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
