from django.contrib import admin
from .models import *
# Register your models here.

class AdminGenre(admin.ModelAdmin):
    list_display = ('genre',)

class AdminUsers(admin.ModelAdmin):
    list_display = ('nom', 'email', 'genre', 'pwd')

class AdminProducteur(admin.ModelAdmin):
    list_display = ('region', 'nom_op', 'producteur_paddy_semences', 'capacite', 'superficie', 'localisation', 'contact', 'site_internet')

class AdminTransformateur(admin.ModelAdmin):
    list_display = ('region', 'nom_transformateur', 'capacite', 'zone_de_transformation', 'localisation', 'contact', 'site_internet')

class AdminImportateur(admin.ModelAdmin):
    list_display = ('region', 'nom_distributeur', 'capacite', 'zone_importation', 'localisation', 'contact', 'site_internet')

class AdminConsommateur(admin.ModelAdmin):
    list_display = ('region', 'nom_association', 'localisation', 'contact', 'site_internet')

class AdminVendeur(admin.ModelAdmin):
    list_display = ('region', 'nom_vendeur', 'type_intrants', 'zone_intervention', 'localisation', 'contact', 'site_internet')

class AdminEtablissement(admin.ModelAdmin):
    list_display = ('region', 'nom_etablissement', 'zone_intervention', 'localisation', 'contact', 'site_internet')

class AdminOffreDemande(admin.ModelAdmin):
    list_display = ('annee', 'population', 'consommateur', 'consommateur_par_tete', 'demande_total', 'offre', 'gap')

class AdminActeurETPotentiel(admin.ModelAdmin):
    list_display = ('acteur', 'superficie_exploite', 'superficie_potentielle', 'production_actuelle', 'production_potentielle')

admin.site.register(Users, AdminUsers)
admin.site.register(Genre, AdminGenre)
admin.site.register(Producteur, AdminProducteur)
admin.site.register(Tranformateur, AdminTransformateur)
admin.site.register(Importateur, AdminImportateur)
admin.site.register(Consommateur, AdminConsommateur)
admin.site.register(Vendeur, AdminVendeur)
admin.site.register(Etablissement, AdminEtablissement)
admin.site.register(OffreDemande, AdminOffreDemande)
admin.site.register(ActeurEtPotentiel, AdminActeurETPotentiel)
