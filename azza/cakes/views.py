from django.http import JsonResponse
from .models import Cake
from .serializers import CakeSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class CakeAPIView(APIView):
    def get(self, request):
        # cakes =  Cake.objects.order_by("-price")
        # cakes =  Cake.objects.get(id=1)
        cakes = Cake.objects.filter(price=8.00)
        serializer = CakeSerializer(cakes, many=True)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
        
    @swagger_auto_schema(
        request_body=CakeSerializer
    )
    def post(self, request):
        serializer = CakeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                 serializer.data,
                 status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

