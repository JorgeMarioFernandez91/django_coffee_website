from django.contrib import admin

# Register your models here.

# this is a relative import,
# it imports the 'Product' class from 'models.py' it is important
# to have 'models.py' and 'admin.py' in the same directory
from .models import Product

# in the django admin page, for the website, we can now 'add' and 
# 'change' 'Products', and each field of 'Products' can be altered 
# manually
admin.site.register(Product)