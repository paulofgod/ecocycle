from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}))
    description = forms.CharField(label="", max_length=1000, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}))
    price = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}))
    whatsapp = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Whatsapp Link'}))
    telephone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    quantity = forms.IntegerField()
    category = forms.ChoiceField(
        choices=Product.CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    image = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image', 'whatsapp', 'telephone']
        

