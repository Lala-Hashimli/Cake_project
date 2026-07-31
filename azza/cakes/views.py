from django.http import JsonResponse
# from .models import Cakes
# Create your views here.


def get_all_cakes(request):
    # cakes =  Cakes.objects.all()

    return JsonResponse({
        "message": "succesfully"
    })

