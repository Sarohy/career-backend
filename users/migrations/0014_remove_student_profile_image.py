# Generated by Django 4.1.3 on 2023-06-21 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_student_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_image',
        ),
    ]
