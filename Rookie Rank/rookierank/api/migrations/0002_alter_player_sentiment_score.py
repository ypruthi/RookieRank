# Generated by Django 4.2.7 on 2023-11-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sentiment_score',
            field=models.IntegerField(),
        ),
    ]
