from django.http import JsonResponse
from .models import Cake
from .serializers import CakeSerializer
from .utils import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .services import CakeService
import random


class CakeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cakes =  CakeService.get_all_cakes()

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

            # send_mail(
            #     subject="Salam",
            #     message="Netersen?"
            # )

            return Response(
                 serializer.data,
                 status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class CakeDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
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
        
# class CacheTestAPIView(APIView):
#     def get(self, request):
#         cache.set(
#             "cake_name",
#             "Chocolate Cake",
#             timeout=15
#         )

#         # value = cache.get("cake_name")
#         cache.delete("cake_name")
        
#         value = cache.get("cake_name")

#         return Response({
#             "value": value
#         })


class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp_code = str(random.randint(1000,9999))
        cache_key = f"otp_{email}"
        
        cache.set(
            cache_key,
            otp_code,
            timeout=60
        )
        
        return Response({
            "message": "otp sent successfully!!!!",
            "otp": otp_code
            }
        )
        

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp_code = request.data.get("otp_code")

        cache_key = f"otp_{email}"
        stored_otp = cache.get(cache_key)

        print("EMAIL:", email)
        print("OTP FROM POSTMAN:", otp_code)
        print("OTP FROM REDIS:", stored_otp)
        print("CACHE KEY:", cache_key)

        if otp_code != stored_otp:
            return Response({
                "error": "invalid otp!!!!!"
            })

        cache.delete(cache_key)

        return Response({
            "message": "verified!!!!"
        })