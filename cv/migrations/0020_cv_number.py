# Generated by Django 4.1.3 on 2023-10-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0019_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
    ]
