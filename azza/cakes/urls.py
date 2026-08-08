from django.urls import path
from .views import CakeAPIView


urlpatterns = [
    path(
        'cakes/', 
        CakeAPIView.as_view(),
        name="cakes"
    )
]



