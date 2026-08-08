from django.db import models
import uuid
# Create your models here.

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

    def __str__(self):
        return self.name
    
    
    
# {
#     "id": 1,
#     "name": "Mars",
#     "price": 11.9
    
# }