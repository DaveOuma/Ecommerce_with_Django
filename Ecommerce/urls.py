from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>', views.customer_detail, name='customer_detail'),
    
]
