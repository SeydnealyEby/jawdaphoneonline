from django.contrib import admin

from BoutiqueEnligne.models import  ChargeurVente, EcouteurVente, Inscrit, PayerProduit, Vente

# Register your models here.
#admin.site.register(Order)
admin.site.register(Vente)
admin.site.register(Inscrit)
admin.site.register(ChargeurVente)
admin.site.register(EcouteurVente)
admin.site.register(PayerProduit)
