# Generated by Django 5.0.7 on 2024-07-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
