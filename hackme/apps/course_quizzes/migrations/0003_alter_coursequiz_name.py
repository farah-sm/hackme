# Generated by Django 5.0.7 on 2024-07-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_quizzes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursequiz',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
