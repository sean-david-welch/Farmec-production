# Generated by Django 4.1.7 on 2023-03-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_rename_short_description_supplier_facts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='short_description',
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]