# Generated by Django 4.1.2 on 2023-01-13 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created']},
        ),
    ]