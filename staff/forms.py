
from django import forms

from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'stock_quantity',
            'expired',
        ]
        labels = {
            "expired":"Expiry Date (YYYY-MM-DD)"
        }