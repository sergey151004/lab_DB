from django.contrib import admin
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

admin.site.register(User)
admin.site.register(UserPhone)
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Courier)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Role)
admin.site.register(UserRole)
