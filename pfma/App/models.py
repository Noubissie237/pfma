from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre

    class Meta:
        db_table = 'Genres'
        verbose_name = "Genre"
        verbose_name_plural = ("Genres")

class Users(models.Model):
    nom = models.CharField(max_length=70)
    email = models.EmailField(max_length=254, unique=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    pwd = models.CharField(max_length=70)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "User"
        verbose_name_plural = ("Users")
        db_table = 'Users'


############################## ACTEURS ##############################
        
    ################# DIRECT #################
class Producteur(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_op = models.CharField(max_length=250, null=True, blank=True)
    producteur_paddy_semences = models.CharField(max_length=250, null=True, blank=True)
    capacite = models.IntegerField(null=True, blank=True)
    superficie = models.IntegerField(null=True, blank=True) 
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Producteur"
        verbose_name_plural = ("Producteurs")
        db_table = "Producteur"



class Tranformateur(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_transformateur = models.CharField(max_length=250, null=True, blank=True)
    capacite = models.IntegerField(null=True, blank=True)
    zone_de_transformation = models.CharField(max_length=250, null=True, blank=True)
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Tranformateur"
        verbose_name_plural = ("Tranformateurs")
        db_table = "Tranformateur"



class Importateur(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_distributeur = models.CharField(max_length=250, null=True, blank=True)
    capacite = models.IntegerField(null=True, blank=True)
    zone_importation = models.CharField(max_length=250, null=True, blank=True)
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Importateur"
        verbose_name_plural = ("Importateurs")
        db_table = "Importateur"



class Consommateur(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_association = models.CharField(max_length=250, null=True, blank=True)
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Consommateur"
        verbose_name_plural = ("Consommateurs")
        db_table = "Consommateur"





        ################# INDIRECT #################
class Vendeur(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_vendeur = models.CharField(max_length=250, null=True, blank=True)
    type_intrants = models.CharField(max_length=250, null=True, blank=True)
    zone_intervention = models.CharField(max_length=250, null=True, blank=True)
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Vendeur"
        verbose_name_plural = ("Vendeurs")
        db_table = "Vendeur"


class Etablissement(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    nom_etablissement = models.CharField(max_length=250, null=True, blank=True)
    zone_intervention = models.CharField(max_length=250, null=True, blank=True)
    localisation = models.CharField(max_length=250, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    site_internet = models.CharField(max_length=150, null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "Etablissement"
        verbose_name_plural = ("Etablissements")
        db_table = "Etablissement"


############################## ACTEURS ##############################

    ################# GENERAL #################

class OffreDemande(models.Model):
    annee = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    consommateur = models.IntegerField(null=True, blank=True)
    consommateur_par_tete = models.FloatField(null=True, blank=True)
    demande_total = models.IntegerField(null=True, blank=True)
    offre = models.IntegerField(null=True, blank=True)
    gap = models.IntegerField(null=True, blank=True)


    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "OffreDemande"
        verbose_name_plural = ("OffreDemandes")
        db_table = "OffreDemande"

class ActeurEtPotentiel(models.Model):
    acteur = models.CharField(max_length=150, null=True, blank=True)
    superficie_exploite = models.IntegerField(null=True, blank=True)
    superficie_potentielle = models.IntegerField(null=True, blank=True)
    production_actuelle = models.IntegerField(null=True, blank=True)
    production_potentielle = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = "ActeurEtPotentiel"
        verbose_name_plural = ("ActeurEtPotentiels")
        db_table = "ActeurEtPotentiel"


####################################################