from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')  # Ajout du champ image à l'affichage

# Ou vous pouvez simplement l'enregistrer comme ceci
# admin.site.register(Product)
