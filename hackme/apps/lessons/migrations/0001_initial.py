# Generated by Django 5.0.7 on 2024-07-28 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('lesson_format', models.CharField(choices=[('text', 'Text'), ('video', 'Video'), ('pdf', 'PDF'), ('text_and_video', 'Text And Video')], default='text', max_length=15)),
                ('lesson_material', models.FileField(blank=True, null=True, upload_to='')),
                ('lesson_text', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='courses.course')),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
    ]
