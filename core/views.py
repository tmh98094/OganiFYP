from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic
from .forms import ContactForm, AddToCartForm
from cart.models import Product
from cart.utils import get_or_set_order_session


class HomeView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    
class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We will reply to your message as soon as possible!")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_message = f"""
            Received message below from {name}, {email}
            ________________________
            {message}
            """
            
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)

