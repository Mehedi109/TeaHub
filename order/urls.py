from django.urls import path
from . import views

urlpatterns = [
    path('cart',views.add_to_cart,name="cart"),
    path('get_cart_data',views.get_cart_data,name="get_cart_data"),
    path('change_quan',views.change_quan,name="change_quan"),
    #path('charge',views.charge),
    path('order',views.order),
    path('customer',views.customer,name="customer"),
    path('customer_details/<int:id>',views.customer_details,name="customer_details"),
    path('customer_cart_data',views.customer_cart_data,name="customer_cart_data"),
    path('customer_delete/<int:id>',views.customer_delete,name='customer_delete'),
]