# Generated by Django 4.1.3 on 2023-03-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('psychometric', '0002_remove_testtype_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychometrictest',
            name='score',
        ),
        migrations.RemoveField(
            model_name='psychometrictest',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(default=0.18181818181818182, on_delete=django.db.models.deletion.CASCADE, to='psychometric.testtype'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychometric.psychometrictest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
    ]
