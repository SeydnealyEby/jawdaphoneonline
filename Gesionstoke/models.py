from django.db import models
from django.utils.timezone import now

class Chargeur(models.Model):
    nomproduit = models.CharField(max_length=100, default="tel")
    type = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    vente_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nomproduit

class Ecouteur(models.Model):
    nomproduit = models.CharField(max_length=100, default="ecouteur")
    type = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits2/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    vente_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nomproduit

class Produit(models.Model):
    nomproduit = models.CharField(max_length=100, default="tel")
    tussi = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    vente_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nomproduit

class Commande(models.Model):
    nameclient = models.CharField(max_length=100)
    numtel = models.IntegerField()
    nametussi = models.CharField(max_length=200)
    dessin = models.CharField(max_length=100)
    description = models.TextField()
    datevenir = models.DateTimeField(default=now)
    daterevenir = models.DateTimeField(default=now, null=True, blank=True)
    photo1 = models.ImageField(upload_to='commandes/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='commandes/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='commandes/', null=True, blank=True)
    telephone_selected = models.BooleanField(default=False)
    chargeur_selected = models.BooleanField(default=False)
    ecouteur_selected = models.BooleanField(default=False)
    client_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nameclient

class Loginn(models.Model):
    username = models.CharField(max_length=100)
    telephonn = models.IntegerField()

    def __str__(self):
        return self.username