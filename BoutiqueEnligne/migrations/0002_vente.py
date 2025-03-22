# Generated by Django 5.1.4 on 2025-02-19 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoutiqueEnligne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproduit', models.CharField(default='tel', max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('prixinit', models.IntegerField(default=0)),
                ('prixtot', models.IntegerField(default=0)),
                ('quantite', models.IntegerField()),
                ('benefice', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits1/')),
            ],
        ),
    ]
