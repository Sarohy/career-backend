# Generated by Django 4.1.3 on 2023-05-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_cv_address_cv_address2_cv_city_cv_eircode_cv_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
