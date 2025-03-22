from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render 
from Gesionstoke.models import Chargeur, Ecouteur, Produit
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import  ChargeurVente, EcouteurVente, Inscrit, PayerProduit, Vente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.utils import timezone
# Create your views here.
def test(req):
    return HttpResponse('selam')

def acceul(req):
    
    lstprod = Produit.objects.all()
    charg= Chargeur.objects.all()
    ecout = Ecouteur.objects.all()
   
    return render(req, 'affichage/accuil.html', {'produits': lstprod, 'chargeurs': charg, 
                                                 'ecouteurs':ecout})
#@login_required(login_url='inscrir')
def checkout(request, prod_id):
    prod = get_object_or_404(Produit, id=prod_id)

    if request.method == "POST":
        return confirmation(request, prod_id)  # Appelle la fonction seulement en cas de POST

    return render(request, "affichage/checkout.html", {'produit': prod})







def confirmation(request, prodsup):
    produitsup = get_object_or_404(Produit, id=prodsup)

    if request.method == "POST":
        # Récupération des données
        nom_client = request.POST.get("nom")
        email_client = request.POST.get("email")
        mode_paiement = request.POST.get("mode_paiement")
        montant = request.POST.get("montant")
        telephone = request.POST.get("telephone")
        produitt = request.POST.get("nomp")
        image = request.POST.get("image")

        # Vérification des champs
        if not all([nom_client, email_client, mode_paiement, montant, telephone, image]):
            return render(request, 'affichage/checkout.html', 
                        {'produit': produitsup, 'error': "Veuillez remplir tous les champs."})

        # Correction du chemin image
        if image.startswith('/media/'):
            image = image.replace('/media/', '')

        # Création du paiement
        try:
            paiement = PayerProduit.objects.create(
                nom=nom_client,
                email=email_client,
                modpayement=mode_paiement,
                montantpayer=montant,
                telephone=telephone,
                produit=produitt,
                image=image,
                date_achat=timezone.now()
            )
            paiement.save()

            # Création de la vente avec lien stock
            vente = Vente.objects.create(
                nomproduit=produitsup.nomproduit, 
                type=produitsup.tussi, 
                prixinit=produitsup.prixinit, 
                prixtot=produitsup.prixtot,
                quantite=1, 
                benefice=produitsup.benefice, 
                image=produitsup.image, 
                description=produitsup.description,
                stock_id=produitsup.id
            )

            # Mise à jour du stock
            if produitsup.quantite > 0:
                if produitsup.quantite == 1:
                    produitsup.delete()
                else:
                    produitsup.quantite -= 1
                    produitsup.vente_id = vente.id
                    produitsup.save()

            return redirect('contactd')

        except Exception as e:
            print("Erreur:", e)
            return render(request, 'affichage/checkout.html', 
                        {'produit': produitsup, 'error': "Erreur lors de l'enregistrement."})

    return render(request, 'affichage/checkout.html', {'produit': produitsup})

def confirmation1(req, chargid):
    chrgd = get_object_or_404(Chargeur, id=chargid)
    
    try:
        # Création de la vente
        chrg = ChargeurVente.objects.create(
            nomproduit=chrgd.nomproduit,
            type=chrgd.type,
            prixinit=chrgd.prixinit,
            prixtot=chrgd.prixtot, 
            quantite=chrgd.quantite,
            benefice=chrgd.benefice,
            image=chrgd.image,
            description=chrgd.description,
            stock_id=chrgd.id
        )
        
        # Mise à jour du stock
        if chrgd.quantite == 1:
            chrgd.delete()
        else:
            chrgd.quantite -= 1
            chrgd.vente_id = chrg.id
            chrgd.save()
            
        return redirect('contactd')
        
    except Exception as e:
        print("Erreur:", e)
        return render(req, 'affichage/checkout1.html', {'charid': chrgd, 'error': "Erreur de traitement"})

def confirmation2(req, ecoutid):
    ecouteur = get_object_or_404(Ecouteur, id=ecoutid)
    
    try:
        # Création de la vente
        vente = EcouteurVente.objects.create(
            nomproduit=ecouteur.nomproduit,
            type=ecouteur.type,
            prixinit=ecouteur.prixinit,
            prixtot=ecouteur.prixtot, 
            quantite=ecouteur.quantite,
            benefice=ecouteur.benefice,
            image=ecouteur.image,
            description=ecouteur.description,
            stock_id=ecouteur.id
        )
        
        # Mise à jour du stock
        if ecouteur.quantite == 1:
            ecouteur.delete()
        else:
            ecouteur.quantite -= 1
            ecouteur.vente_id = vente.id
            ecouteur.save()
            
        return redirect('contactd')
        
    except Exception as e:
        print("Erreur:", e)
        return render(req, 'affichage/checkout2.html', 
                     {'ecouid': ecouteur, 'error': "Erreur de traitement"})
def send_order_email(client_email, numero_livreur, matricule_vehicule):
    subject = "Confirmation de votre commande - Jawdaphone 📦"
    message = f"""
Bonjour,

Votre commande a été confirmée avec succès ! 🚀

📦 Le livreur arrivera bientôt avec votre produit.

📞 Numéro du livreur : {numero_livreur}
🚗 Matricule du véhicule : {matricule_vehicule}

Merci d’avoir commandé chez Jawdaphone ! 😊

Cordialement,
L'équipe Jawdaphone.
"""
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [client_email],
            fail_silently=False,
        )
        print("E-mail envoyé avec succès à", client_email)
    except Exception as e:
        print("Erreur lors de l'envoi de l'e-mail :", str(e))



def sinscrir(request):
    if request.method == 'POST':
        nomu = request.POST.get('nom')
        telphoneu = request.POST.get('telphone')
        emailu = request.POST.get('email')
        passwordu = request.POST.get('password')

        # Vérifier si l'email existe déjà
        if Inscrit.objects.filter(email=emailu).exists():
            return render(request, 'pageslogin/sinscrir.html', {'error': 'Email déjà utilisé'})

        # Création de l'utilisateur avec mot de passe haché
        user = Inscrit(username=emailu, email=emailu)
        user.set_password(passwordu)  # Hacher le mot de passe correctement
        user.telphone = telphoneu  # Si ton modèle Inscrit contient ce champ
        user.save()
        return redirect('acceil')
        # Authentification automatique après inscription
        user = authenticate(request, username=emailu, password=passwordu)
        if user:
            login(request, user)

        return redirect('telephone')  # Rediriger vers la boutique après inscription

    return render(request, 'pageslogin/sinscrir.html')


def contact(req):
    
    return render(req,'affichage/contact.html')

    
def chargeur(req):
    charg= Chargeur.objects.all()
    
    return render(req,'affichage/chargeur.html', {'chargeurs':charg})

def checkout1(req,  charg_id):
    char= get_object_or_404(Chargeur, id= charg_id)
    return render(req,'affichage/checkout1.html', {'charid':char})



def telephone(req):

    tel = Produit.objects.all()
    return render(req, 'affichage/telephones.html', {'telphones': tel})

def ecouteur(req):
    ecou = Ecouteur.objects.all()
    return render(req,'affichage/ecouteur.html', {'ecouteurs':ecou})

def checkout2(req,ecout_id):
    ecout= get_object_or_404(Ecouteur, id= ecout_id)
    return render(req,'affichage/checkout2.html', {'ecouid':ecout})


def detail(req, id_dtail):
    produit = Produit.objects.filter(id=id_dtail).first()
    chargeur = Chargeur.objects.filter(id=id_dtail).first()
    ecouteur = Ecouteur.objects.filter(id=id_dtail).first()

    if produit:
        return render(req, 'affichage/dtail.html', {'item': produit, 'type': 'produit'})
    elif chargeur:
        return render(req, 'affichage/dtail.html', {'item': chargeur, 'type': 'chargeur'})
    elif ecouteur:
        return render(req, 'affichage/dtail.html', {'item': ecouteur, 'type': 'ecouteur'}) 
    else:
        return render(req, 'affichage/404.html')

        

def contacteznous(req):
    
    return render(req, 'affichage/contanter.html')

def notification(req):
    notf = PayerProduit.objects.all()  # Tri par date
    return render(req, 'affichage/notification.html', {'notification': notf})

def propos(req):
    
    return render(req, 'affichage/apropos.html')
