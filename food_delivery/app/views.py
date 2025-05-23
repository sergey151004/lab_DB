from rest_framework import viewsets
from .models import (
    User,
    UserPhone,
    Address,
    Restaurant,
    MenuItem,
    Courier,
    Order,
    OrderItem,
    Role,
    UserRole,
)
from .serializers import (
    UserSerializer,
    UserPhoneSerializer,
    AddressSerializer,
    RestaurantSerializer,
    MenuItemSerializer,
    CourierSerializer,
    OrderSerializer,
    OrderItemSerializer,
    RoleSerializer,
    UserRoleSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPhoneViewSet(viewsets.ModelViewSet):
    queryset = UserPhone.objects.all()
    serializer_class = UserPhoneSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


# core/views.py
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")
