from django.contrib import admin
from .models import Customer, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
