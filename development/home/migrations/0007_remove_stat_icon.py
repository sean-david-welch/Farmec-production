# Generated by Django 4.1.2 on 2023-01-09 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_stat_svg_alter_stat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='icon',
        ),
    ]
