# Generated by Django 4.1.3 on 2024-01-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0036_alter_additionalinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='additional_info',
            field=models.TextField(max_length=300),
        ),
    ]
