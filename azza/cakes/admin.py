from django.contrib import admin
from .models import Cake, Category, Ingredients

# Register your models here.
admin.site.register(Cake)
admin.site.register(Category)
admin.site.register(Ingredients)