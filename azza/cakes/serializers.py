from rest_framework import serializers
from .models import Cake, Category, Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
            model = Recipe
            fields = "__all__"



class CakeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    class Meta:
        model = Cake
        fields = [
             "id",
             "name",
             "price",
             "recipe",

        ]   
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
        
    
