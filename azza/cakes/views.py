from django.http import JsonResponse
from .models import Cake
from .serializers import CakeSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404


class CakeAPIView(APIView):
    def get(self, request):
        cakes =  Cake.objects.all()
        
        search =  request.query_params.get("search")
        
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        
        if search:
            cakes = cakes.filter(name__icontains=search)
            
        if min_price:
            cakes = cakes.filter(price__gte=min_price)
            
        if max_price:
            cakes = cakes.filter(price__lt=max_price)
            
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
    

class CakeDetailAPIView(APIView):
    def get(self, request, pk):
        cake = get_object_or_404(
            Cake,
            pk=pk
        )
        serializer = CakeSerializer(cake)    
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):

        cake = get_object_or_404(
            Cake,
            pk=pk
        )

        serializer = CakeSerializer(
            cake,
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        cake = get_object_or_404(
            Cake,
            pk=pk,
        )

        serializer = CakeSerializer(
            cake,
            data=request.data, 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        cake = get_object_or_404(
            Cake,
            pk=pk
        )

        cake.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
"""
price__gte - greater than and equeal >=
price__lte  less than and equeal

price__gt  - greater than
price__lt - less than



__  lookup operator
  
name__contains="s"

"""


