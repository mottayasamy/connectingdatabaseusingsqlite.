from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        Product.objects.create(name=name, price=price, quantity=quantity, description=description)
        return HttpResponse("Product created successfully")
    return render(request, 'create_product.html')

def read_products(request):
    products = Product.objects.all()
    return render(request, 'read_products.html', {'products': products})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.description = request.POST.get('description')
        product.save()
        return HttpResponse("Product updated successfully")
    return render(request, 'update_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return HttpResponse("Product deleted successfully")
    return render(request, 'delete_product.html', {'product': product})
