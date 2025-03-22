# Generated by Django 5.1.4 on 2025-02-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gesionstoke', '0006_chargeur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecouteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproduit', models.CharField(default='ecouteur', max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('prixinit', models.IntegerField(default=0)),
                ('prixtot', models.IntegerField(default=0)),
                ('quantite', models.IntegerField()),
                ('benefice', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits2/')),
            ],
        ),
    ]
