# Generated by Django 4.1.2 on 2022-12-09 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0010_sipfact_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sipfact',
            name='heading',
        ),
    ]