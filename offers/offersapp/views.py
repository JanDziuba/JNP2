from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OfferSerializer
from .models import Offer


@api_view(['POST'])
def add_offer(request):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_offers(request):
    price_from = request.POST.get('price-from', 0)
    price_to = request.POST.get('price-to', float('inf'))
    size_from = request.POST.get('size-from', 0)
    size_to = request.POST.get('size-to', float('inf'))

    if price_from == '':
        price_from = 0
    if price_to == '':
        price_to = float('inf')
    if size_from == '':
        size_from = 0
    if size_to == '':
        size_to = float('inf')

    offers = Offer.objects.filter(price__range=(price_from, price_to),
                                  size__range=(size_from, size_to)).values()
    return Response({'data': offers}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_offer(request, id):
    offer = Offer.objects.get(id=id)
    return Response({'data': OfferSerializer(offer).data}, status=status.HTTP_200_OK)
