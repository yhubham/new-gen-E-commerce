from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.filter(is_available=True)
    
    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context)

def product_detail(request, slug):
    # Fetch the product by its slug, or return a 404 error if not found
    product = get_object_or_404(Product, slug=slug, is_available=True)
    
    return render(request, 'store/detail.html', {'product': product})