from django.urls import path
from .views import *

urlpatterns = [
    path('api/add_offer', add_offer, name="add_offer"),
    path('api/get_offers', get_offers, name="get_offers"),
    path('api/get_offer/<int:id>', get_offer, name='get_offer'),
]
