from django.urls import path
from.views import home,Utilisateur,Membre,Reunion,grouptontine,paiement,Add,Edit,Edit1,Update,Delete,Supprimer,Ajouter


urlpatterns = [
    path('',home, name= "index"),
    path("utilisateur/",Utilisateur, name= "utilisateur"),
    path("paiement/",paiement, name= "paiement"),
    path("reunion/",Reunion, name= "reunion"),
    path("membre/",Membre, name= "membre"),
    path("grouptontine/", grouptontine, name="grouptontine"),
    path("add/", Add, name="add"),
    path("ajou/", Ajouter, name="ajou"),
    path("edit/", Edit, name="edit"),
    path("edit1/", Edit1, name="edit1"),
    path("update/<str:id>/", Update, name="update"),
    path("delete/<int:id>/", Delete, name="delete"),
    path("supprimer/<int:id>/", Supprimer, name="supprimer"),
]