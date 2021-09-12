from django.urls import path
from .views import *

urlpatterns = [
    path('api/get_messages', get_messages, name="get_messages"),
]
