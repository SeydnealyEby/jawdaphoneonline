# Generated by Django 5.1.4 on 2025-03-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gesionstoke', '0015_alter_commande_datevenir'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entreesorie',
        ),
        migrations.DeleteModel(
            name='Livreur',
        ),
        migrations.DeleteModel(
            name='Sortie',
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
