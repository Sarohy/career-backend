# Generated by Django 4.1.3 on 2023-03-10 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('cv', '0009_remove_reference_contactemail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='experience',
            name='position',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='position',
        ),
        migrations.AddField(
            model_name='experience',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='jobtitle',
            field=models.CharField(choices=[('1', 'ASSISTANT'), ('2', 'WORK SHADOW'), ('3', 'OTHER')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='area_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='user_title',
            field=models.CharField(choices=[('1', 'MR'), ('2', 'MRS'), ('3', 'MS')], max_length=1),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
            options={
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Qualities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
            options={
                'verbose_name_plural': 'qualities',
            },
        ),
        migrations.AlterField(
            model_name='reference',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.jobtitle'),
        ),
    ]
