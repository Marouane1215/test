# Generated by Django 5.1.2 on 2024-11-11 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_remove_jobmachine_id_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmachine',
            name='ID_machine',
            field=models.IntegerField(default=1, verbose_name='ID de la Machine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='ID_job',
            field=models.IntegerField(unique=True, verbose_name='ID du Job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='d',
            field=models.IntegerField(blank=True, null=True, verbose_name='Date de livraison'),
        ),
        migrations.AlterField(
            model_name='job',
            name='r',
            field=models.IntegerField(verbose_name="Date d'arrivée"),
        ),
        migrations.RemoveField(
            model_name='jobmachine',
            name='job',
        ),
        migrations.AlterField(
            model_name='jobmachine',
            name='p',
            field=models.IntegerField(verbose_name='Temps de traitement'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='CONSTRAINT',
            field=models.CharField(blank=True, choices=[(None, 'Aucune contrainte'), ('delivery', 'Date de livraison'), ('prep_time', 'Temps de préparation'), ('no_wait', 'No wait'), ('no_idle', 'No idle')], max_length=20, null=True, verbose_name='Contrainte'),
        ),
        migrations.AddField(
            model_name='jobmachine',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='page.job'),
            preserve_default=False,
        ),
    ]
