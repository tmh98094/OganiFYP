from django import forms
from django_countries.widgets import CountrySelectWidget
from cart.models import OrderItem


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your e-mail"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your message'
    }))
    
class AddToCartForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']