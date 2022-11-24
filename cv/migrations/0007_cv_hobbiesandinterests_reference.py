# Generated by Django 4.1.3 on 2022-11-24 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('cv', '0006_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='HobbiesandInterests',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnumber', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('contactemail', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
    ]
