from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name="home_view"),
    path('login/', login_view, name="login_view"),
    path('new-offer/', new_offer_view, name="new_offer_view"),
    path('detail/<int:id>', product_detail_view, name="product_detail_view"),
    path('action/login/', action_login, name="action_login"),
    path('action/register/', action_register, name="action_register"),
    path('action/logout/', action_logout, name="action_logout"),
    path('action/add_product/', action_add_product, name="action_add_product"),
]
