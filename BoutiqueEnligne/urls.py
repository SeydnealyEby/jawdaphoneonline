from django.urls import path

from BoutiqueEnligne import views
from Gesionstoke.views import ajoutercommande

urlpatterns =[
    path('test/', views.test, ),
    path('acceul/', views.acceul, name="acceil"),
    path("checkout/<int:prod_id>", views.checkout, name="checkout"),
    path("checkout1/<int:charg_id>", views.checkout1, name="checkout1"),
    path("checkout2/<int:ecout_id>", views.checkout2, name="checkout2"),
    path("confirmation/<int:prodsup>", views.confirmation, name="confirmation"),
    path("confirmation1/<int:chargid>", views.confirmation1, name="confirmation1"),
    path("confirmation2/<int:ecoutid>", views.confirmation2, name="confirmation2"),
    path('inscrir/', views.sinscrir, name="sinscrit"),
    path("cotact/", views.contact, name="contactd"),
    path('chargeur/', views.chargeur, name="cherg"),
    path('telephone/', views.telephone, name="tel"),
    path('ecouteur/', views.ecouteur, name="ecouteur"),
    path('detail/<int:id_dtail>', views.detail, name="details"),
    path('ajouterC/',ajoutercommande,name="AjouterC"),
    path('contacter/',views.contacteznous,name="contacter"),
    path('notification/',views.notification,name="notificatio"),
    path('apropos/',views.propos,name="prop"),
    
    
]