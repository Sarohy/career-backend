# Generated by Django 4.1.3 on 2024-01-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_student_number'),
        ('cv', '0035_alter_juniorcerttest_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]