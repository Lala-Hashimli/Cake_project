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
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cakes",
        null=True,
        blank=True
    )
    
    ingredients = models.ManyToManyField(
        Ingredients,
        related_name='cakes',
        blank=True
    )

    def __str__(self):
        return self.name
    

