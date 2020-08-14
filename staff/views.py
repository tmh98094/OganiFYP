from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse,redirect
from django.views import generic
from cart.models import Order, Product, Category
from .forms import ProductForm, OrderForm
from .mixins import StaffUserMixin


class StaffView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/staff.html'
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by = 10
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super(StaffView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context

class OrderCollectView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/order_collect.html'
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by = 10
    context_object_name = 'orders'
    def get_context_data(self, **kwargs):
        context = super(OrderCollectView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context
    
class ConfirmCollectView(LoginRequiredMixin, StaffUserMixin, generic.UpdateView):
    template_name = 'staff/confirm_collect.html'
    queryset = Order.objects.all()
    form_class = OrderForm
    context_object_name = 'orders'

    def form_valid(self, form):
        form.save()
        return redirect("staff:staff")
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmCollectView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context
    
class ProductListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/product_list.html'
    queryset = Product.objects.all()
    paginate_by = 10
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context

class ProductCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(ProductCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context

class ProductUpdateView(LoginRequiredMixin, StaffUserMixin, generic.UpdateView):
    template_name = 'staff/product_update.html'
    form_class = ProductForm
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")

    def form_valid(self, form):
        form.save()
        return super(ProductUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context

        
class ProductDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name = 'staff/product_delete.html'
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")
    
    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context