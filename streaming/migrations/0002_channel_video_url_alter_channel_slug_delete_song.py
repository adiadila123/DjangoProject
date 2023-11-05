# Generated by Django 4.0.8 on 2023-10-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]