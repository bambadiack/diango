from django.db import models

# Create your models here.
class Utilisateurs(models.Model):
    nom = models.CharField(max_length = 100)
    prenom =models.CharField(max_length = 100)
    email =models.EmailField(max_length = 100,null=True,blank=True)
    Mot_de_passe = models.CharField(max_length = 100)

    def __str__(self):
       return f" {self.prenom} {self.nom} {self.email} {self.Mot_de_passe}"

class GroupesTontine(models.Model):
    nom = models.CharField(max_length = 100)
    description = models.TextField(null=True, max_length=400, blank=True)

    def __str__(self):
       return f" {self.nom} "


class Membres(models.Model):
    utilisateur_id = models.IntegerField()
    groupe_tontine_id = models.IntegerField()
    auteur = models.ForeignKey(Utilisateurs,on_delete=models.CASCADE)
    auteur = models.ForeignKey(GroupesTontine,on_delete=models.CASCADE)

    def __str__(self):
       return f" {self.utilisateur_id} {self.groupe_tontine_id} {self.auteur}"
    

class paiements(models.Model):
    membre_id = models.IntegerField()
    montant = models.DecimalField(max_digits=10,decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(Membres,on_delete=models.CASCADE)

    def __str__(self):
       return f" {self.membre_id} {self.montant} {self.date_paiement} {self.auteur}"
    

class Reunions(models.Model):
    groupe_tontine_id = models.IntegerField()
    date_reunion = models.DateField(auto_now_add=True)
    lieu = models.CharField(max_length=100)
    ordre_du_jour = models.TextField(null=True, max_length=400, blank=True)
    auteur = models.ForeignKey(GroupesTontine,on_delete=models.CASCADE)    

    def __str__(self):
       return f" {self.groupe_tontine_id} {self.date_reunion} {self.lieu} {self.ordre_du_jour} {self.auteur}"
    