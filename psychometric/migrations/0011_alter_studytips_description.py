# Generated by Django 4.1.3 on 2024-04-16 08:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychometric', '0010_alter_answer_answer_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studytips',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
