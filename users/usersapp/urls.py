from django.urls import path
from .views import *

urlpatterns = [
    path('api/login', login, name="login"),
    path('api/register', register, name="register"),
    path('api/products', products, name="products"),
    path('api/products/<int:id>', products_id, name='products_id'),
]
