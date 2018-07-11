# Generated by Django 2.0.5 on 2018-07-08 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflowApp', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='college',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='degree',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
