from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('bmi',views.bmi, name='bmi'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('products',views.products,name='products'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('create_order/',views.createOrder,name='create_order'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),
]