# Generated by Django 4.1.2 on 2023-01-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0016_alter_machineregistration_date_yyyy_mm_dd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineregistration',
            name='date_YYYY_MM_DD',
        ),
        migrations.AddField(
            model_name='machineregistration',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]