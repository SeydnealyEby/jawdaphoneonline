# Generated by Django 5.1.4 on 2025-03-20 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gesionstoke', '0013_commande_chargeur_selected_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='avance',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='prix',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='restavance',
        ),
    ]
