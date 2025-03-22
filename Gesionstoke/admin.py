from django.contrib import admin
from .models import Chargeur, Ecouteur, Produit,Commande,Loginn


admin.site.register(Produit)

admin.site.register(Commande)

admin.site.register(Loginn)

admin.site.register(Chargeur)
admin.site.register(Ecouteur)
#admin.site.register(Livreur)

