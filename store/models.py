from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('plastic', 'Plastic'),
        ('rubber', 'Rubber'),
        ('tin', 'Tin'),
        ('old_cloths', 'Old Cloths'),
        ('metal', 'Metal'),
        ('paper', 'Paper'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='plastic'
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who posted the product
    created_at = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Optionally, add an image field for product images
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

