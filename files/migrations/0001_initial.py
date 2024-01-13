# Generated by Django 5.0.1 on 2024-01-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('user_link', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
