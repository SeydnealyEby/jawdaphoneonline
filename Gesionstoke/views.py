from datetime import datetime
from django.core.exceptions import ValidationError
import re
#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from BoutiqueEnligne.models import ChargeurVente, EcouteurVente, Vente

from .models import Chargeur, Ecouteur, Produit,  Commande,Loginn
from django.contrib.auth.decorators import login_required





Inscription_key = "jawdaphon@@@"
def adminsapp(req):
    if req.method == 'POST':
        utilisateur = req.POST.get('usernames')
        phone = req.POST.get('telephones')
        inscrit = req.POST.get('inscription_key')

        if inscrit != Inscription_key :
           # messages.error(req,"Clé d'inscription incorrecte.")

            return render(req,'ajmosup/adminpage.html')
        Loginn.objects.create(username=utilisateur, telephonn=phone)
        #messages.success(req, "Utilisateur ajouté avec succès.")

        return redirect('acceul')
    
    return render(req,'ajmosup/adminpage.html')


from django.shortcuts import render, redirect
from .models import Loginn  # Assurez-vous que Loginn est bien importé

def adminappnktt(req):
    # If user is already logged in, redirect to home
    if 'user_id' in req.session:
        return redirect('acceul')

    if req.method == 'POST':
        utilisateur0 = req.POST.get('usernames0')
        phone0 = req.POST.get('telephones0')

        try:
            utilisateur = Loginn.objects.get(username=utilisateur0, telephonn=phone0)
            
            # Create session
            req.session['user_id'] = utilisateur.id
            req.session['username'] = utilisateur.username
            
            # Set session expiry - 24 hours
            req.session.set_expiry(86400)
            
            messages.success(req, f'Bienvenue, {utilisateur.username}!')
            return redirect('acceul')
        
        except Loginn.DoesNotExist:
            messages.error(req, 'Nom d\'utilisateur ou numéro de téléphone incorrect')
            return render(req, 'ajmosup/adminapps.html', {
                'error': True,
                'username': utilisateur0  # Keep the username in form
            })
    
    return render(req, 'ajmosup/adminapps.html')

# Add this logout function
def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
        messages.success(request, 'Vous avez été déconnecté avec succès')
    return redirect('admin_app0')

# Add this login required decorator
def login_required(view_func):
    def wrapper(req, *args, **kwargs):
        if 'user_id' not in req.session:
            messages.warning(req, 'Veuillez vous connecter pour accéder à cette page')
            return redirect('admin_app0')
        return view_func(req, *args, **kwargs)
    return wrapper


@login_required
def ajouterProd(request):
    if request.method == 'POST':
        # Récupération des données
        quantite = request.POST.get('quantie')
        nomprod1 = request.POST.get('nomprod')
        tussi = request.POST.get('tussi')
        prixachat1 = request.POST.get('prixachat')
        prixvente1 = request.POST.get('prixvente')
        benefice1 = request.POST.get('benefice')
        photo = request.FILES.get('imagep')
        desc = request.POST.get('description')

        # Chargeur
        if nomprod1.lower().startswith(("char", "chargeur")):
            chargeur = Chargeur.objects.create(
                quantite=quantite,
                nomproduit=nomprod1, 
                type=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                benefice=benefice1,
                image=photo, 
                description=desc
            )
            # Création vente associée
            vente = ChargeurVente.objects.create(
                nomproduit=nomprod1,
                type=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                quantite=quantite,
                benefice=benefice1,
                image=photo,
                description=desc,
                stock_id=chargeur.id
            )
            chargeur.vente_id = vente.id
            chargeur.save()
            return redirect('lstcharg')

        # Écouteur
        elif nomprod1.lower().startswith(("ecouteur", "ecou")):
            ecouteur = Ecouteur.objects.create(
                quantite=quantite,
                nomproduit=nomprod1, 
                type=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                benefice=benefice1,
                image=photo,
                description=desc
            )
            # Création vente associée
            vente = EcouteurVente.objects.create(
                nomproduit=nomprod1,
                type=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                quantite=quantite,
                benefice=benefice1,
                image=photo,
                description=desc,
                stock_id=ecouteur.id
            )
            ecouteur.vente_id = vente.id
            ecouteur.save()
            return redirect('lstecout')
        
        # Téléphone
        else:
            produit = Produit.objects.create(
                quantite=quantite,
                nomproduit=nomprod1, 
                tussi=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                benefice=benefice1,
                image=photo, 
                description=desc
            )
            # Création vente associée
            vente = Vente.objects.create(
                nomproduit=nomprod1,
                type=tussi,
                prixinit=prixachat1,
                prixtot=prixvente1,
                quantite=quantite,
                benefice=benefice1,
                image=photo,
                description=desc,
                stock_id=produit.id
            )
            produit.vente_id = vente.id
            produit.save()
            return redirect('listbou')

    return render(request, 'ajmosup/AjouterProduit.html')
@login_required
def listproduit(request):
    prodt =Produit.objects.all()
    return render(request,'ajmosup/ListProduit.html',{'prodL':prodt})
@login_required
def modifiertel(request, tel_idm):
    # Récupérer l'objet ou afficher une erreur 404 s'il n'existe pas
    prodm = get_object_or_404(Produit, id=tel_idm)

    if request.method == 'POST':
        # Récupérer les données soumises via POST
        quantite = request.POST.get('quantite')
        tussi = request.POST.get('tussi')
        prod1 = request.POST.get('modprod')
        prixa1 = request.POST.get('prixac')
        prixv1 = request.POST.get('prixv')
        benefice1 = request.POST.get('benefice')
        desc = request.POST.get('description')
       
        if 'image' in request.FILES:
            prodm.image = request.FILES['image']
        # Mettre à jour l'objet Boubou
        prodm.quantite = quantite
        prodm.tussi = tussi
        prodm.nomproduit = prod1
        prodm.prixinit = prixa1
        prodm.prixtot = prixv1
        prodm.benefice = benefice1
        prodm.description = desc
        prodm.save()  # Sauvegarder les modifications

        # Rediriger vers une page (par exemple, la liste des boubous)
        return redirect('listbou')

    # Passer les données actuelles au template
    return render(request, 'ajmosup/modifiertelephone.html', {'modfiertel': prodm})
@login_required
def supprimertel(request,tel_ids):
   
    boubous = Produit.objects.get(id = tel_ids)
    boubous.delete()
    return redirect('listbou')
   # boubou1 =Boubou.objects.all()
   # return render(request,'ajmosup/listBoubou.html',{'boubouL':boubou1})
@login_required



@login_required
def acceul(req):
    return render(req, 'ajmosup/accueill.html')



def ajoutercommande(req):
    if req.method == 'POST':
        try:
            # Get selected products
            produits_selectionnes = req.POST.getlist('produits[]')

            # Create command
            commande = Commande(
                nameclient=req.POST.get('nomclient'),
                numtel=req.POST.get('numtelephone'),
                nametussi=', '.join(produits_selectionnes),
                dessin=req.POST.get('nomdessin'),
                description=req.POST.get('descriptionen'),
                datevenir=req.POST.get('datevenir'),
                daterevenir=req.POST.get('daterevenir'),
                telephone_selected='telephone' in produits_selectionnes,
                chargeur_selected='chargeur' in produits_selectionnes,
                ecouteur_selected='ecouteur' in produits_selectionnes
            )

            # Handle photos
            if 'photo1' in req.FILES:
                commande.photo1 = req.FILES['photo1']
            if 'photo2' in req.FILES:
                commande.photo2 = req.FILES['photo2']
            if 'photo3' in req.FILES:
                commande.photo3 = req.FILES['photo3']

            commande.save()
            messages.success(req, "Commande ajoutée avec succès.")
            return redirect('listCl')

        except Exception as e:
            messages.error(req, f"Erreur lors de l'ajout de la commande : {str(e)}")
            return render(req, 'ajmosup/ajouterCommande.html', {
                'form_data': req.POST
            })

    return render(req, 'ajmosup/ajouterCommande.html')
@login_required
def  listclients(req):

    client = Commande.objects.all()


    return render(req, 'ajmosup/listclient.html', {'tableclient':client})
@login_required
def modifierclient(req, client_ids):
    client = get_object_or_404(Commande, id=client_ids)
    
    if req.method == 'POST':
        try:
            # Informations client
            client.nameclient = req.POST.get('nomclient')
            client.numtel = req.POST.get('numtelephone')
            
            # Produits sélectionnés
            produits_selectionnes = req.POST.getlist('produits[]')
            client.nametussi = ', '.join(produits_selectionnes)
            
            # Détails
            client.dessin = req.POST.get('nomdessin')
            client.description = req.POST.get('descriptionen')
            
            # Date de retour
            daterevenir_str = req.POST.get('daterevenir')
            if daterevenir_str:
                client.daterevenir = datetime.strptime(daterevenir_str, '%Y-%m-%dT%H:%M')

            # Gestion des photos
            if 'photo1' in req.FILES:
                if client.photo1:
                    client.photo1.delete()
                client.photo1 = req.FILES['photo1']
            
            if 'photo2' in req.FILES:
                if client.photo2:
                    client.photo2.delete()
                client.photo2 = req.FILES['photo2']
            
            if 'photo3' in req.FILES:
                if client.photo3:
                    client.photo3.delete()
                client.photo3 = req.FILES['photo3']

            client.save()
            messages.success(req, 'Modifications enregistrées avec succès!')
            return redirect('listCl')
            
        except Exception as e:
            messages.error(req, f'Erreur: {str(e)}')
            return render(req, 'ajmosup/modifierCommande.html', {
                'client1': client,
                'error': str(e)
            })

    context = {
        'client1': client,
        'nametussi_list': client.nametussi.split(', ') if client.nametussi else []
    }
    return render(req, 'ajmosup/modifierCommande.html', context)
@login_required      
def suppclient(req,clientsup):
    clientsup = Commande.objects.get(id = clientsup)
    clientsup.delete()

    return redirect('listCl')


  
@login_required
def listvent(req):
    
    lstv = Vente.objects.all()
    return render(req,'ajmosup/listevente.html', {'prodL':lstv})
@login_required
def modifiervent(req, modf_id):
    modv = get_object_or_404(Vente, id=modf_id)
    if req.method == 'POST':
        # Récupération des données du formulaire
        nom = req.POST.get('modprod')
        typev = req.POST.get('type')
        prixacv = req.POST.get('prixac')
        prixvv = req.POST.get('prixv')
        quantitev = req.POST.get('quantite')
        desc = req.POST.get('description')
        beneficev = req.POST.get('benefice')
        images = req.FILES.get('image')
        
        # Mise à jour de l'objet Vente
        modv.nomproduit = nom
        modv.type = typev
        modv.prixinit = prixacv
        modv.prixtot = prixvv
        modv.quantite = quantitev
        modv.benefice = beneficev
        modv.description = desc
        
        if images:
            modv.image = images

        # Mise à jour du stock lié si existe
        if modv.stock_id:
            try:
                produit = Produit.objects.get(id=modv.stock_id)
                produit.quantite = quantitev
                produit.prixinit = prixacv
                produit.prixtot = prixvv
                produit.benefice = beneficev
                produit.save()
            except Produit.DoesNotExist:
                pass
                
        modv.save()
        return redirect('listvte')
        
    return render(req, 'ajmosup/modifierlstvent.html', {'prod': modv})
@login_required
def supprimerv(req, sup_id):
    prodsup = get_object_or_404(Vente, id=sup_id)
    
    # Mise à jour du stock lié
    if prodsup.stock_id:
        try:
            produit = Produit.objects.get(id=prodsup.stock_id)
            produit.vente_id = None
            produit.save()
        except Produit.DoesNotExist:
            pass
            
    prodsup.delete()
    return redirect('listvte')

@login_required
def listchargeur(req):
    lstchrg = Chargeur.objects.all()
    return render(req, 'ajmosup/listChargeur.html', {'prodLc':lstchrg})
@login_required
def modifierchergeur(request, modchar):
    # Récupérer l'objet ou afficher une erreur 404 s'il n'existe pas
    prodm = get_object_or_404(Chargeur, id=modchar)

    if request.method == 'POST':
        # Récupérer les données soumises via POST
        quantite = request.POST.get('quantite')
        tyepc = request.POST.get('type')
        prod1 = request.POST.get('modprod')
        prixa1 = request.POST.get('prixac')
        prixv1 = request.POST.get('prixv')
        benefice1 = request.POST.get('benefice')
        des = request.POST.get('description')
       
        if 'image' in request.FILES:
            prodm.image = request.FILES['image']
     
        prodm.quantite = quantite
        prodm.type = tyepc
        prodm.nomproduit = prod1
        prodm.prixinit = prixa1
        prodm.prixtot = prixv1
        prodm.benefice = benefice1
        prodm.description = des
        prodm.save()  # Sauvegarder les modifications

        # Rediriger vers une page (par exemple, la liste des boubous)
        return redirect('lstcharg')

    # Passer les données actuelles au template
    return render(request, 'ajmosup/modifierChargeur.html', {'charheur': prodm})
@login_required
def supprimerchargeur(req,sup_chag):
    sup = get_object_or_404(Chargeur, id=sup_chag)
    sup.delete()
    return redirect('lstcharg')
@login_required
def ventechargeur(req):
    lstchar =ChargeurVente.objects.all()
    return render(req, "ajmosup/listchargeurvent.html", {'lstchar':lstchar})

@login_required   
def modifierchergeurv(request,modcharv):
    prodm = get_object_or_404(ChargeurVente, id=modcharv)

    if request.method == 'POST':
        # Récupérer les données soumises via POST
        quantite = request.POST.get('quantite')
        tyepc = request.POST.get('type')
        prod1 = request.POST.get('modprod')
        prixa1 = request.POST.get('prixac')
        prixv1 = request.POST.get('prixv')
        desc = request.POST.get('description')
        benefice1 = request.POST.get('benefice')
       
        if 'image' in request.FILES:
            prodm.image = request.FILES['image']
     
        prodm.quantite = quantite
        prodm.type = tyepc
        prodm.nomproduit = prod1
        prodm.prixinit = prixa1
        prodm.prixtot = prixv1
        prodm.benefice = benefice1
        prodm.description = desc
        prodm.save()  # Sauvegarder les modifications

      
        return redirect('ventechar')
    return render(request, 'ajmosup/modifierchargeurvente.html', {'charheurv': prodm})
@login_required
def supprimerchergeurv(req,modcharvs):
    supv = get_object_or_404(ChargeurVente, id=modcharvs)
    supv.delete()
    return redirect('ventechar')
@login_required
def lstecouteur(req):
    lstec= Ecouteur.objects.all()
    return render(req,'ajmosup/lstecouteur.html',{'ecouteur':lstec})
    
def suprimerecouteur(req,supecou):
    supecout= Ecouteur.objects.get(id=supecou)
    supecout.delete()
    return redirect('lstecout')

@login_required
def modifierecouteur(request,modecou):
    prodm = get_object_or_404(Ecouteur, id=modecou)

    if request.method == 'POST':
        # Récupérer les données soumises via POST
        quantite = request.POST.get('quantite')
        tyepc = request.POST.get('type')
        prod1 = request.POST.get('modprod')
        prixa1 = request.POST.get('prixac')
        prixv1 = request.POST.get('prixv')
        desc = request.POST.get('description')
        benefice1 = request.POST.get('benefice')
       
        if 'image' in request.FILES:
            prodm.image = request.FILES['image']
     
        prodm.quantite = quantite
        prodm.type = tyepc
        prodm.nomproduit = prod1
        prodm.prixinit = prixa1
        prodm.prixtot = prixv1 
        prodm.benefice = benefice1
        prodm.description = desc
        prodm.save()  # Sauvegarder les modifications

      
        return redirect('lstecout')
    return render(request, 'ajmosup/modifierecouteur.html', {'ecouteur': prodm})
@login_required
def lstecouteurv(req):
    lstv= EcouteurVente.objects.all()
    return render(req,'ajmosup/lstecouteurvent.html', {'ecoutv':lstv})

@login_required
def modecouteurv(request,mod_v):
    prodm = get_object_or_404(EcouteurVente, id=mod_v)

    if request.method == 'POST':
        # Récupérer les données soumises via POST
        quantite = request.POST.get('quantite')
        tyepc = request.POST.get('type')
        prod1 = request.POST.get('modprod')
        prixa1 = request.POST.get('prixac')
        prixv1 = request.POST.get('prixv')
        desc = request.POST.get('description')
        benefice1 = request.POST.get('benefice')
       
        if 'image' in request.FILES:
            prodm.image = request.FILES['image']
     
        prodm.quantite = quantite
        prodm.type = tyepc
        prodm.nomproduit = prod1
        prodm.prixinit = prixa1
        prodm.prixtot = prixv1
        prodm.benefice = benefice1
        prodm.description = desc
        prodm.save()  # Sauvegarder les modifications

      
        return redirect('lstecouts')
    return render(request, 'ajmosup/modifierecouteurvente.html', {'ecouteurv': prodm})
@login_required
def supprimerecouteurv(req,modecouvs):
    supv = get_object_or_404(EcouteurVente, id=modecouvs)
    supv.delete()
    return redirect('lstecouts')




    
    
    


