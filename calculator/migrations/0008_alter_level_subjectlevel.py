# Generated by Django 4.1.3 on 2023-08-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_userpoints_total_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='subjectlevel',
            field=models.CharField(choices=[('higher', 'Higher'), ('ordinary', 'Ordinary'), ('foundation', 'Foundation')], max_length=10),
        ),
    ]
