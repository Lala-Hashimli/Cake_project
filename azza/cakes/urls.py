from django.urls import path
from .views import CakeAPIView, CakeDetailAPIView


urlpatterns = [
    path(
        'cakes/', 
        CakeAPIView.as_view(),
        name="cakes"
    ),
    path(
        'cakes/<int:pk>/',
        CakeDetailAPIView.as_view(),
        name="detailed-cake"
    )
]



