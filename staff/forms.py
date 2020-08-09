
from django import forms

from cart.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'nutrition',
            'price',
            'stock_quantity',
            'pickup_location',
            'produced',
            'expired',
            'primary_category',
            'secondary_categories',
        ]
        labels = {
            'title' :"Product Name",
            'image':"Product Image",
            'description' : "Description",
            'nutrition':'Nutrition Fact (Please line space and separate each nutrition value)',
            "price":"Price (5000 = RM 50.00)",
            "produced":"Produced Date (YYYY-MM-DD)",
            'stock_quantity' : "Stock Quantity",
            'pickup_location': "Pick-up Location",
            "expired":"Expiry Date (YYYY-MM-DD)",
            'primary_category':'Primary Category',
            'secondary_categories':'Secondary Categories'
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'collected'
        ]
        labels = {
            "collected":"Order Collected?"
        }