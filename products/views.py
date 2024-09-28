from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def list_products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  # 3 produits par page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'list_products.html', {'products': products})

def modify_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'modify_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    
    return render(request, 'confirm_delete.html', {'product': product})
