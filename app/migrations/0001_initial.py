# Generated by Django 5.2.4 on 2025-07-25 08:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialCheckbook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('checkbook', models.FileField(upload_to='checkbooks/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Minuites',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('1de4fd98-f2bc-4f9e-b87a-4fd8bb9ad835'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('minuites', models.FileField(upload_to='minuites/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
