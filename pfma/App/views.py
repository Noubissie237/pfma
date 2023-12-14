from django.shortcuts import render
from .forms import UsersForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def direct(request):
    return render(request, 'acteurs/direct.html')

def indirect(request):
    return render(request, 'acteurs/indirect.html')

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

def general(request):
    return render(request, 'sir/general.html')

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
            form.save()
            return render(request, 'needRegistration/home.html')
        
    form = UsersForm()
    return render(request, "logOrReg/registration.html", {"form" : form})

@login_required
def privateHome(request):
    return render(request, 'needRegistration/home.html')