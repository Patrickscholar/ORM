# Generated by Django 5.2 on 2025-05-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=150, primary_key='True', serialize=False)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
