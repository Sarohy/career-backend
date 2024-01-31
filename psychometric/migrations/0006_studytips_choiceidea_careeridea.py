# Generated by Django 4.1.3 on 2024-01-31 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psychometric', '0005_psychometrictest_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1400)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychometric.testtype')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.TextField(blank=True, max_length=1400, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychometric.testtype')),
            ],
        ),
        migrations.CreateModel(
            name='CareerIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.TextField(blank=True, max_length=1400, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychometric.testtype')),
            ],
        ),
    ]
