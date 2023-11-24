# Generated by Django 4.2.7 on 2023-11-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('playerID', models.CharField(max_length=5, unique=True)),
                ('sentiment_score', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]