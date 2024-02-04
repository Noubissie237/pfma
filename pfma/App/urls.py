from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('direct/', direct, name="Acteurs directs"),
    path('indirect/', indirect, name="Acteurs indirects"),
    path('institutionnel/', institutionnel, name="Acteurs institutionnels"),
    path('bibliotheque/', bibliotheque, name="bibliotheque"),
    path('caracteristique/', caracteristique, name="caracteristique"),
    path('composition/', composition, name="composition"),
    path('contrainte/', contrainte, name="contrainte"),
    path('definition/', definition, name="definition"),
    path('intervention/', intervention, name="intervention"),
    path('justification/', justification, name="justification"),
    path('objectif/', objectif, name="objectif"),
    path('resultat/', resultat, name="resultat"),
    path('utilite/', utilite, name="utilite"),
    path('hand/', hand, name="hand"),
    path('commercial/', commercial, name="commercial"),
    path('general/', general, name="general"),
    path('technique/', technique, name="technique"),
    path('mediatheque/', mediatheque, name="madiatheque"),
    path('conference/', conference, name="Video Conference"),
    path('inscription/', formRegistration, name="inscription à la plateforme"),
    path('accueil/', privateHome, name="Accueil des membres enregistrés"),
    
]