# Generated by Django 4.1.3 on 2023-04-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='', max_length=700, null=True),
        ),
    ]
