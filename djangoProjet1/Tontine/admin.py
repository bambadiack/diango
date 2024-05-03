from django.contrib import admin

# Register your models here.
from .models import Utilisateurs,GroupesTontine,Membres,paiements,Reunions

admin.site.register(Utilisateurs)
admin.site.register(GroupesTontine)
admin.site.register(Membres)
admin.site.register(paiements)
admin.site.register(Reunions)