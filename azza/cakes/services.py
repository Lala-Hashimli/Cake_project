from .models import Cake
from django.shortcuts import get_object_or_404


class CakeService:
    @staticmethod
    def get_all_cakes():
        return Cake.objects.all()
    
    @staticmethod
    def get_cake_by_id(pk):
        return get_object_or_404(Cake, pk=pk)
    
    @staticmethod
    def update_cake_status(cake):
        if cake.stock == 0:
            cake.status = "sold"
            cake.save()
        return cake
    
    @staticmethod
    def get_active_cakes(cake):
        return Cake.objects.filter(
            status="active"
        ) 

    @staticmethod
    def update_stock(cake, stock):
        cake.stock = stock
        if stock == 0:
            cake.status = "sold"
        else:
            cake.status = "active"
            
        cake.save()
        return cake
    
    # @staticmethod
    # def change_status(cake, new_status):
    #     old_status = cake.status
    #     cake.status = new_status
    #     cake.save()
        
    #     if old_status != new_status:
    #         send_mail_task.delay(cake.id)
    #     return(cake)