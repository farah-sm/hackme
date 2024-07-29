# Generated by Django 5.0.7 on 2024-07-28 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_quizzes', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_courses',
            },
        ),
        migrations.CreateModel(
            name='UserCourseTopicQuizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_course_topic_quizzes',
            },
        ),
        migrations.CreateModel(
            name='UserCourseTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_course_topics',
            },
        ),
        migrations.CreateModel(
            name='UserExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('solution', models.TextField()),
                ('progress', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_exercises',
            },
        ),
        migrations.CreateModel(
            name='UserLessonQuizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_lesson_quizzes',
            },
        ),
        migrations.CreateModel(
            name='UserLessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_lessons',
            },
        ),
        migrations.CreateModel(
            name='UserCourseQuizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('course_quiz', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='course_quizzes.coursequiz')),
            ],
            options={
                'db_table': 'user_course_quizzes',
            },
        ),
    ]
