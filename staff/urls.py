  
from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
     path('', views.StaffView.as_view(), name='staff'),
     path('collect/', views.OrderCollectView.as_view(), name='order-collect'),
     path('collect/<pk>/confirm/', views.ConfirmCollectView.as_view(), name='confirm-collect'),
     path('create/', views.ProductCreateView.as_view(), name='product-create'),
     path('products/', views.ProductListView.as_view(), name='product-list'),
     path('products/<pk>/update/',views.ProductUpdateView.as_view(), name='product-update'),
     path('products/<pk>/delete/',views.ProductDeleteView.as_view(), name='product-delete'),
]