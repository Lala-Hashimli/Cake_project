from django.db import models
import uuid

    
class Category(models.Model):    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Cake(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected")
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/")
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cakes",
        null=True,
        blank=True
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    
    ingredients = models.ManyToManyField(
        Ingredients,
        related_name='cakes',
        blank=True
    )

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    cake = models.OneToOneField(
        Cake,
        on_delete= models.SET_NULL,
        null=True,
        related_name="recipe"
    )
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()

    def __str__(self):
        return f"{self.cake.name} recipe"