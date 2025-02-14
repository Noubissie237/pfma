# Generated by Django 4.2.6 on 2024-02-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_rename_demande_totale_offredemande_demande_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offredemande',
            name='annee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='consommateur',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='consommateur_par_tete',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='demande_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='gap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='offre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offredemande',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
