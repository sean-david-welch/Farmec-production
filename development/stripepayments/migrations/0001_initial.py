# Generated by Django 4.1.2 on 2023-02-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StripeProduct',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='product_files/')),
                ('url', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
