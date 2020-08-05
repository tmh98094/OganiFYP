from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic
from .forms import ContactForm
from cart.models import Product, Order, Category, User
from cart.utils import get_or_set_order_session
from django.db.models import Q



class OrderView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account.html'

    def get_success_url(self):
        return reverse("account")

class HomeView(generic.ListView):
    template_name = 'index.html'
    
    def get_queryset(self):
        qs = Product.objects.all()
        category = self.request.GET.get('category', None)
        if category:
            qs = qs.filter(Q(primary_category__name=category) |
                        Q(secondary_categories__name=category)).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context
 
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

