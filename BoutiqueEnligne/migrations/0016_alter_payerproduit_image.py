# Generated by Django 5.1.4 on 2025-03-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoutiqueEnligne', '0015_alter_payerproduit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payerproduit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produits/'),
        ),
    ]
