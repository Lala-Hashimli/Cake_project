from django.contrib import admin
from .models import Cake, Category, Ingredients, Recipe

# Register your models here.
admin.site.register(Cake)
admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(Recipe)