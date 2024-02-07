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


############################## SIR ##############################

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

class Documents_sir(models.Model):
    nom = models.CharField(max_length=250)
    fichier = models.FileField(upload_to="staticfiles/documents", max_length=100)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Documents_sir"
        verbose_name_plural = "Documents_sir"
        db_table = "Documents_sir"


################# COMMERCIAL #################
class EvolutionRiz(models.Model):
    annee = models.IntegerField()
    sud = models.IntegerField(null=True, blank=True)
    centre = models.IntegerField(null=True, blank=True)
    est = models.IntegerField(null=True, blank=True)
    ouest = models.IntegerField(null=True, blank=True)
    littoral = models.IntegerField(null=True, blank=True)
    sud_ouest = models.IntegerField(null=True, blank=True)
    nord_ouest = models.IntegerField(null=True, blank=True)
    adamaoua = models.IntegerField(null=True, blank=True)
    nord = models.IntegerField(null=True, blank=True)
    extreme_nord = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.annee
    
    class Meta:
        verbose_name = "Evolution_Riz"
        verbose_name_plural = "Evolution_Riz"
        db_table = "Evolution_Riz"
        
####################################################
        
############# Bibliotheque ############# 
class Documents_bibliotheque(models.Model):
    nom = models.CharField(max_length=250)
    fichier = models.FileField(upload_to="staticfiles/documents", max_length=100)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Documents_bibliotheque"
        verbose_name_plural = "Documents_bibliotheque"
        db_table = "Documents_bibliotheque"


############# Hand in Hand ############# 
class Documents_Hand_in_Hand(models.Model):
    nom = models.CharField(max_length=250)
    fichier = models.FileField(upload_to="staticfiles/documents", max_length=100)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Documents_Hand_in_Hand"
        verbose_name_plural = "Documents_Hand_in_Hand"
        db_table = "Documents_Hand_in_Hand"


############# Mediatheque ############# 
class Images_Mediatheque(models.Model):
    titre = models.CharField(max_length=250)
    image = models.ImageField(upload_to="staticfiles/images", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.titre
    
    class Meta:
        verbose_name = "Images_Mediatheque"
        verbose_name_plural = "Images_Mediatheque"
        db_table = "Images_Mediatheque"


############# Liens ############# 
class Liens(models.Model):
    titre = models.CharField(max_length=250)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.titre
    
    class Meta:
        verbose_name = "Liens"
        verbose_name_plural = "Liens"
        db_table = "Liens"

