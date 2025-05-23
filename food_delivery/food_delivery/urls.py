"""
URL configuration for food_delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers
from django.contrib import admin


from app.views import (
    UserViewSet,
    UserPhoneViewSet,
    AddressViewSet,
    RestaurantViewSet,
    MenuItemViewSet,
    CourierViewSet,
    OrderViewSet,
    OrderItemViewSet,
    RoleViewSet,
    UserRoleViewSet,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"phones", UserPhoneViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"restaurants", RestaurantViewSet)
router.register(r"menu-items", MenuItemViewSet)
router.register(r"couriers", CourierViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"order-items", OrderItemViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"user-roles", UserRoleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
