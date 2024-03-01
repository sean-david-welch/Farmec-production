# Generated by Django 4.1.2 on 2022-12-09 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0011_remove_sipfact_heading'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SipFact',
            new_name='Fact',
        ),
        migrations.RemoveField(
            model_name='sulkyfact',
            name='supplier',
        ),
        migrations.AlterModelOptions(
            name='fact',
            options={'ordering': ['created']},
        ),
        migrations.DeleteModel(
            name='MxFact',
        ),
        migrations.DeleteModel(
            name='SulkyFact',
        ),
    ]
