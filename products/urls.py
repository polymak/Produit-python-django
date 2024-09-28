from django.urls import path
from .views import home, add_product, list_products, modify_product, delete_product

urlpatterns = [
    path('', home, name='home'),
    path('add_product/', add_product, name='add_product'),
    path('list_products/', list_products, name='list_products'),
    path('modify_product/<int:id>/', modify_product, name='modify_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
]
