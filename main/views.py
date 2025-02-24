from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.db.models import Q
from store.models import Product


# Create your views here.

def home(request):
    # Fetch the 3 latest products
    latest_products = Product.objects.all().order_by('-created_at')[:3]
    
    return render(request, 'index.html', {'latest_products': latest_products})

def about(request):
    return render(request, 'about.html', {})



    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('create_product')  # Redirect to post product page if the user is already logged in

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('create_product')  # Redirect to post product page after successful login
        else:
            messages.error(request, ("There was an error, please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after successful registration
            return redirect('create_product')  # Redirect to product creation page
    else:
        messages.success(request, ("Fill out the form properly"))
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

# def search_view(request):
#     query = request.GET.get('q')  # Get the search query from the GET request

#     if query:
#         # Use icontains to perform a case-insensitive search in product name and description
#         products = Product.objects.filter(
#             name__icontains=query
#         ) | Product.objects.filter(
#             description__icontains=query
#         )
#     else:
#         products = Product.objects.all()  # If no query, return all products

#     return render(request, 'product/search_results.html', {'products': products, 'query': query})
    


def search_view(request):
    if request.method == "GET":
        # Get the search term from the GET query parameters
        searched = request.GET.get('q', '')  # Default to empty string if no query is provided

        if searched:
            # Query the products in the model DB
            searched_products = Product.objects.filter(
                Q(name__icontains=searched) | Q(description__icontains=searched)
            )
            
            if not searched_products.exists():
                messages.info(request, "No products found matching your search.")
                return render(request, 'search.html', {'searched': searched, 'products': []})
            else:
                return render(request, 'search.html', {'searched': searched, 'products': searched_products})
        
        else:
            # If the search term is empty, render the empty form without a message
            return render(request, 'search.html', {'searched': '', 'products': []})
    
    else:
        # If the method isn't GET, redirect to the home page or return empty results
        return render(request, 'search.html', {'searched': '', 'products': []})
