# Generated by Django 5.0.7 on 2024-08-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
