# Generated by Django 4.1.3 on 2024-08-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_setquizlimit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setquizlimit',
            name='user',
        ),
    ]
