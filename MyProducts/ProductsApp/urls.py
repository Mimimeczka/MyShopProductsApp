from django.urls import path, include
from rest_framework import routers
from ProductsApp import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]