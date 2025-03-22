from django.urls import path
from .import views
from BoutiqueEnligne.views import notification
urlpatterns = [
    path('login/',views.adminsapp, name = "login"),
    path('logout/', views.logout, name='logout'),
    path('',views.acceul, name="acceul"),
    
    path('adminapp0/', views.adminappnktt, name ="admin_app0"),
    path('ajouterb/', views.ajouterProd, name="ajouterbou"),
    path('listb/', views.listproduit, name="listbou"),
    path('modfier/<int:tel_idm>', views.modifiertel, name="modfierB"),
    path('delete/<int:tel_ids>', views.supprimertel, name="supprimerB"),
    
    path('ajouterC/',views.ajoutercommande,name="AjouterC"),
    path('listclient/', views.listclients, name="listCl"),
    path('modifierclient/<int:client_ids>',views.modifierclient, name="modifierCl"),
    path('supprimerclient/<int:clientsup>',views.suppclient, name="supprimercli"),
    
    path('listvent/', views.listvent , name="listvte"),
    path('modifiervent/<int:modf_id>', views.modifiervent , name="modfv"),
    path('supprimerv/<int:sup_id>', views.supprimerv, name="supprimerv"),
    path('listchargeur/',views.listchargeur, name="lstcharg"),
    path('modfierschar/<int:modchar>',views.modifierchergeur, name="modfcha"),
    path('supprimerchar/<int:sup_chag>', views.supprimerchargeur, name="supchar"),
    path('ventecharg/', views.ventechargeur, name="ventechar"),
    path('modfierscharvente/<int:modcharv>',views.modifierchergeurv, name="modfchav"),
    path('supprimercharvente/<int:modcharvs>',views.supprimerchergeurv, name="supprimerlv"),
    path('lstecouteur/',views.lstecouteur, name="lstecout"),
    path('suprimerecout/<int:supecou>', views.suprimerecouteur, name="supecout"),
    path('modifierecout/<int:modecou>', views.modifierecouteur, name="modecout"),
    path('lstecoutv/', views.lstecouteurv, name="lstecouts"),
    path('modecoutv/<int:mod_v>', views.modecouteurv, name="modecoutvent"),
    path('supprimerecouvente/<int:modecouvs>',views.supprimerecouteurv, name="supprimerecouv"),
    path('notification/', notification, name="notification"),
    


    
    
]