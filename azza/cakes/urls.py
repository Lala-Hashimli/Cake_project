from django.urls import path
from .views import CakeAPIView, CakeDetailAPIView, CacheTestAPIView


urlpatterns = [
    path(
        'cakes/', 
        CakeAPIView.as_view(),
        name="cakes"
    ),
    path(
        'cakes/<uuid:pk>/',
        CakeDetailAPIView.as_view(),
        name="detailed-cake"
    ),
    path(
        'cache-test/',
        CacheTestAPIView.as_view()
    ),
]



