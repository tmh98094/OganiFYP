from django.contrib import admin
from .models import Product, OrderItem, Order, Address, Payment, Category

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = [
    'user',
    'id',
    'ordered',
    'collected',
    ]
    
admin.site.register(Address, AddressAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
