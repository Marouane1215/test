# Generated by Django 5.1.2 on 2024-11-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_jobmachine_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contraint',
            name='session_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planningoption',
            name='session_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
