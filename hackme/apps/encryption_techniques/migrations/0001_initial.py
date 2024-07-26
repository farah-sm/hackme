# Generated by Django 5.0.7 on 2024-07-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptionTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('encryption_type', models.CharField(choices=[('symmetric', 'Symmetric'), ('asymmetric', 'Asymmetric')], default='symmetric', max_length=10)),
            ],
            options={
                'db_table': 'encryption_techniques',
            },
        ),
    ]
