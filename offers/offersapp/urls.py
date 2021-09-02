from django.urls import path
from .views import *

urlpatterns = [
    path('offers/add_offer', add_offer, name="add_offer"),
    path('offers/get_offers', get_offers, name="get_offers"),
    path('offers/get_offer/<int:id>', get_offer, name='get_offer'),
]
