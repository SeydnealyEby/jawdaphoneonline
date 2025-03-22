from django.db import models
from django.utils import timezone

class Vente(models.Model):
    nomproduit = models.CharField(max_length=100, default="tel")
    type = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits1/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    stock_id = models.IntegerField(null=True, blank=True)

class Inscrit(models.Model):
    nom = models.CharField(max_length=100)
    telphone = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
    def get_commandes(self):
        from Gesionstoke.models import Commande
        return Commande.objects.filter(client_id=self.id)

class ChargeurVente(models.Model):
    nomproduit = models.CharField(max_length=100, default="tel")
    type = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    stock_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nomproduit

class EcouteurVente(models.Model):
    nomproduit = models.CharField(max_length=100, default="tel")
    type = models.CharField(max_length=100)
    prixinit = models.IntegerField(default=0)
    prixtot = models.IntegerField(default=0)
    quantite = models.IntegerField()
    benefice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits2v/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    stock_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nomproduit

class PayerProduit(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    modpayement = models.CharField(max_length=100)
    montantpayer = models.IntegerField()
    telephone = models.CharField(max_length=100)
    produit = models.CharField(max_length=100, default="prod")
    image = models.ImageField(upload_to='produits/', null=True, blank=True)
    date_achat = models.DateTimeField(default=timezone.now)
    commande_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nom