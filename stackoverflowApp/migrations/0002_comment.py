# Generated by Django 2.0.5 on 2018-06-25 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stackoverflowApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stackoverflowApp.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stackoverflowApp.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
