from django.http import JsonResponse
from .models import Cake
from .serializers import CakeSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_all_cakes(request):
    cakes =  Cake.objects.all()
    
    serializer = CakeSerializer(cakes, many=True)

    return JsonResponse(serializer.data, safe=False)

