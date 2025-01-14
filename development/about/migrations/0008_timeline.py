# Generated by Django 4.1.2 on 2022-12-10 16:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_rename_staff_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
