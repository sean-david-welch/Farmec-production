# Generated by Django 4.1.2 on 2023-01-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SparePart',
            new_name='Supplier',
        ),
        migrations.AlterModelOptions(
            name='machineregistration',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='warrantyclaim',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='machineregistration',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='warrantyclaim',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
