# Generated by Django 5.1.4 on 2025-03-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gesionstoke', '0011_ecouteur_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesf', models.CharField(max_length=100)),
                ('datecommence', models.DateTimeField()),
                ('saleur', models.IntegerField(default=0)),
                ('mariculv', models.CharField(max_length=100)),
                ('numv', models.IntegerField(default=0)),
            ],
        ),
    ]
