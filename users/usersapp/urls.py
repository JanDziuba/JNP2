from django.urls import path
from .views import *

urlpatterns = [
    path('users/login', login, name="login"),
    path('users/register', register, name="register"),
]
