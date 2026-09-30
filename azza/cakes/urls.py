from django.urls import path
from .views import ( CakeAPIView, CakeDetailAPIView,SendOTPView,
                    VerifyOTPView, AddToBookmarkAPIView, UserBookmarkAPIView)
# , CacheTestAPIView


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
    path("send-otp/",
        SendOTPView.as_view()),
    path("verify-otp/",
         VerifyOTPView.as_view()),

    #BOOKMARK
    path("bookmarks/", 
        UserBookmarkAPIView.as_view(),
        name="user-bookmark"),

    path("cakes/<uuid:cake_pk>/bookmark/",
        AddToBookmarkAPIView.as_view(),
        name="cake-bookmark")

    
    
]



