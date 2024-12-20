# Generated by Django 5.1.2 on 2024-11-03 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_probleme_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_job', models.IntegerField(unique=True)),
                ('d', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_machine', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='probleme',
            name='machine_number',
            field=models.IntegerField(default=0, verbose_name='Numéro de machine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='probleme',
            name='CONSTRAINT',
            field=models.CharField(choices=[('arrival', "Date d'arrivée"), ('delivery', 'Date de livraison'), ('prep_time', 'Temps de préparation')], max_length=20, null=True, verbose_name='Contrainte'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='job_number',
            field=models.IntegerField(verbose_name='Numéro de job'),
        ),
        migrations.CreateModel(
            name='JobMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.job')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.machine')),
            ],
            options={
                'unique_together': {('job', 'machine')},
            },
        ),
    ]
