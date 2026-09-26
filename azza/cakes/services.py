from .models import Cake


class CakeService:
    @staticmethod
    def get_all_cakes():
        return Cake.objects.all()

    