from django.contrib import admin
from .models import Product, CartItem, Testimonial

# Register your models here.
admin.site.register(Product)
admin.site.register(Testimonial)