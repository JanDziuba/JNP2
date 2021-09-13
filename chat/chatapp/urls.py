from django.urls import path
from .views import *

urlpatterns = [
    path('chat/get_messages', get_messages, name="get_messages"),
]
