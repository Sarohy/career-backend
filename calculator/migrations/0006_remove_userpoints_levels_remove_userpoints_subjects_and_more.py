# Generated by Django 4.1.3 on 2023-05-26 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_remove_userpoints_grades_remove_userpoints_levels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoints',
            name='levels',
        ),
        migrations.RemoveField(
            model_name='userpoints',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='userpoints',
            name='total_points',
        ),
    ]
