# Generated by Django 4.1.7 on 2023-03-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
        migrations.AddField(
            model_name='product',
            name='facts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Fact',
        ),
    ]