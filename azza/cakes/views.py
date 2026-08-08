from django.http import JsonResponse
from .models import Cake
from .serializers import CakeSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView



class CakeAPIView(APIView):
    def get(self, request):
        # cakes =  Cake.objects.order_by("-price")
        # cakes =  Cake.objects.get(id=1)
        cakes = Cake.objects.filter(price=8.00)
        serializer = CakeSerializer(cakes, many=True)
        
        return Response(serializer.data)
        
   
