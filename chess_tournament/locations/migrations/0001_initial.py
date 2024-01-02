# Generated by Django 4.1 on 2023-12-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
