from django.urls import path
from .views import get_all_cakes


urlpatterns = [
    path('cakes/', get_all_cakes)
]