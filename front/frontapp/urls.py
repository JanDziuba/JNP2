from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name="home_view"),
    path('login/', login_view, name="login_view"),
    path('new-offer/', new_offer_view, name="new_offer_view"),
    path('room/', room_view, name="room_view"),
    path('detail/<int:id>', offer_detail_view, name="offer_detail_view"),
]
