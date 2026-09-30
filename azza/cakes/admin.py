from django.contrib import admin
from .models import Cake, Category, Ingredients, Recipe, Bookmark

# Register your models here.
admin.site.register(Cake)
admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(Bookmark)