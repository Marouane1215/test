# Generated by Django 5.1.2 on 2024-11-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_job_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmachine',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID de la Session'),
        ),
    ]
