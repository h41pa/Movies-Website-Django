# Generated by Django 5.0.4 on 2024-04-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(upload_to='movie_videos/'),
        ),
    ]