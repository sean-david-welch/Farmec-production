# Generated by Django 4.1.2 on 2023-01-20 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0014_alter_machineregistration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machineregistration',
            old_name='date',
            new_name='date_YYYY_MM_DD',
        ),
    ]
