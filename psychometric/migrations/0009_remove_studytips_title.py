# Generated by Django 4.1.3 on 2024-04-01 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychometric', '0008_alter_psychometrictest_intro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytips',
            name='title',
        ),
    ]
