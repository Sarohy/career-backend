# Generated by Django 4.1.3 on 2023-10-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_quiz_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Quiz_images'),
        ),
    ]
