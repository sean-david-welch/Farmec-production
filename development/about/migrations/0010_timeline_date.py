# Generated by Django 4.1.2 on 2023-01-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_employee_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
