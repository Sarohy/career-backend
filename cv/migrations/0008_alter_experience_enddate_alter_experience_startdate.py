# Generated by Django 4.1.3 on 2023-05-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_experience_is_current_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
