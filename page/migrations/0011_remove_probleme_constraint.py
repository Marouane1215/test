# Generated by Django 5.1.2 on 2024-11-14 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_contraint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probleme',
            name='CONSTRAINT',
        ),
    ]
