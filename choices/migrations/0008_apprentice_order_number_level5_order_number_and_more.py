# Generated by Django 4.1.3 on 2023-08-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0007_remove_level8_order_level8_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprentice',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='level5',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='level6',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='other',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
