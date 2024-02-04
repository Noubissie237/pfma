from django.shortcuts import render
from .forms import UsersForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def direct(request):
    producteurs = Producteur.objects.all()
    transformateurs = Tranformateur.objects.all()
    importateurs = Importateur.objects.all()
    consommateurs = Consommateur.objects.all()

    context = {
        'producteurs' : producteurs,
        'transformateurs' : transformateurs,
        'importateurs' : importateurs,
        'consommateurs' : consommateurs
    }

    return render(request, 'acteurs/direct.html', context={'data' : context})

def indirect(request):
    vendeurs = Vendeur.objects.all()
    etablissements = Etablissement.objects.all()

    context = {
        'vendeurs' : vendeurs,
        'etablissements' : etablissements
    }

    return render(request, 'acteurs/indirect.html', context={'data' : context})

def general(request):
    data = OffreDemande.objects.all()
    acteur_et_potentielle = ActeurEtPotentiel.objects.all()
    sommeSuperficieExploite = 0
    sommeSuperficePotentielle = 0
    sommeProductionActuelle = 0
    sommeProductionPotentielle = 0
    list_somme = []
    for elt in acteur_et_potentielle:
        sommeSuperficieExploite += elt.superficie_exploite
        sommeSuperficePotentielle += elt.superficie_potentielle
        sommeProductionActuelle += elt.production_actuelle
        sommeProductionPotentielle += elt.production_potentielle
    

    
    context = {
        'OffreDemande' : data,
        'acteur_et_potentielle' : acteur_et_potentielle,
        'sommeSuperficieExploite' : sommeSuperficieExploite,
        'sommeSuperficePotentielle' : sommeSuperficePotentielle,
        'sommeProductionActuelle' : sommeProductionActuelle,
        'sommeProductionPotentielle' : sommeProductionPotentielle,
    }

    return render(request, 'sir/general.html', context={'data' : context})

def institutionnel(request):
    return render(request, 'acteurs/institutionnel.html')

def bibliotheque(request):
    return render(request, 'biblio/livreTechnique.html')

def caracteristique(request):
    return render(request, 'descriptifs/caracteristique.html')

def composition(request):
    return render(request, 'descriptifs/composition.html')

def contrainte(request):
    return render(request, 'descriptifs/contrainte.html')

def definition(request):
    return render(request, 'descriptifs/definition.html')

def intervention(request):
    return render(request, 'descriptifs/intervention.html')

def justification(request):
    return render(request, 'descriptifs/justification.html')

def objectif(request):
    return render(request, 'descriptifs/objectif.html')

def resultat(request):
    return render(request, 'descriptifs/resultat.html')

def utilite(request):
    return render(request, 'descriptifs/utilite.html')

def hand(request):
    return render(request, 'hand/hand.html')

def commercial(request):
    return render(request, 'sir/commercial.html')


def technique(request):
    return render(request, 'sir/technique.html')

def mediatheque(request):
    return render(request, 'mediatheque/mediatheque.html')

def conference(request):
    return render(request, 'conference/index.html')

def formRegistration(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            print(data['nom'])
            return render(request, 'needRegistration/home.html', context={"User" : form.cleaned_data['nom']})
        
    form = UsersForm()
    return render(request, "logOrReg/registration.html", {"form" : form})

@login_required
def privateHome(request):
    return render(request, 'needRegistration/home.html')