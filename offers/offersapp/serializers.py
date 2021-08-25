from rest_framework import serializers
from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'title', 'size', 'price', 'description',
                  'seller_username', 'seller_id')
