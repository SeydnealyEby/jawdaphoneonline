# Generated by Django 5.1.4 on 2025-03-20 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gesionstoke', '0014_remove_commande_avance_remove_commande_prix_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='datevenir',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
