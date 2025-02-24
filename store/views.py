from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product


# Create your views here.

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES for image upload
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Assign the current user as the seller
            product.save()
            return redirect('product_list')  # Redirect to a page displaying the products
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def agents(request):
    return render(request, 'agents.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_category(request):
    category = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'category.html', {'category': category})

def products_by_category(request, category_name):
    # Get all products that belong to the selected category
    products = Product.objects.filter(category=category_name)
    return render(request, 'category_list.html', {'products': products, 'category_name': category_name})