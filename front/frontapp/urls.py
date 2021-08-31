from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name="home_view"),
    path('login/', login_view, name="login_view"),
    path('new-offer/', new_offer_view, name="new_offer_view"),
    path('room/', room_view, name="room_view"),
    path('detail/<int:id>', offer_detail_view, name="offer_detail_view"),
    path('action/login/', action_login, name="action_login"),
    path('action/register/', action_register, name="action_register"),
    path('action/logout/', action_logout, name="action_logout"),
    path('action/add_offer/', action_add_offer, name="action_add_offer"),
    path('action/get_offers/', action_get_offers, name="action_get_offers"),
]
