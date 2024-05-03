from django.shortcuts import render,redirect
from Tontine.models import GroupesTontine
from Tontine.models import Membres
from Tontine.models import Utilisateurs
from Tontine.models import paiements
from Tontine.models import Reunions



# Create your views here.
def home(request):
    return render(request, "index.html")

def Membre(request):
    return render(request, "membre.html")

def Utilisateur(request):
    return render(request, "utilisateur.html")

def paiement(request):
    return render(request, "paiement.html")

def Reunion(request):
    return render(request, "reunion.html")



def grouptontine(request):
    emp = GroupesTontine.objects.all()
    context ={
        'emp':emp,
    }
    return render(request, "grouptontine.html",context)

def Membre(request):
    empdata = Membres.objects.all()
    context ={
        'emp':empdata,
    }
    return render(request, "membre.html",context)


def Utilisateur(request):
    empdata = Utilisateurs.objects.all()
    context ={
        'emp':empdata,
    }
    return render(request, "utilisateur.html",context)


def paiement(request):
    emp = paiements.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, "paiement.html",context)


def Reunion(request):
    emp = Reunions.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, "reunion.html",context)

def Add(request):
    if request.method == "POST":
        Nom = request.POST.get('Nom')
        Description = request.POST.get('Description')

        emp = GroupesTontine(
            nom = Nom,
            description = Description,
        )
        emp.save()
        return redirect('grouptontine')
    

    return render(request, "grouptontine.html")


def Ajouter(request):
    if request.method == "POST":
        Nom = request.POST.get('Nom')
        Prenom = request.POST.get('prenom')
        Email = request.POST.get('Email')
        Mot_de_passe = request.POST.get('Mot_de_passe')

        empdata = Utilisateurs(
            nom = Nom,
            prenom = Prenom,
            email = Email,
            Mot_de_passe = Mot_de_passe,
            
        )
        empdata.save()
        return redirect('utilisateur')
    

    return render(request, "utilisateur.html")

 

def Edit(request):
    emp = GroupesTontine.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, "grouptontine.html" ,context)

def Edit1(request):
    emp = Utilisateurs.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, "utilisateur.html" ,context)

def Update(request,id):
    if request.method == "POST":
        Nom = request.POST.get('nom')
        Description = request.POST.get('description')

        emp = GroupesTontine(
            id = id,
            nom = Nom,
            description = Description,
        )
        emp.save()
        return redirect('grouptontine')
    

    return render(request, 'grouptontine.html'),


def Delete(request,id):
    
    empdata = GroupesTontine.objects.filter(id=id)
    empdata.delete()

    
    return redirect("grouptontine")

def Supprimer(request,id):
    
    empdata = Utilisateurs.objects.filter(id=id)
    empdata.delete()

    
    return redirect("utilisateur")

