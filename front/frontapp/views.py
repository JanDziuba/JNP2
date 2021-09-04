from django.shortcuts import render
import requests


def home_view(request):
    response = requests.get('http://offers/offers/get_offers')
    context = {'offers': response.json()['data']}
    return render(request, 'frontapp/home.html', context)


def offer_detail_view(request, id):
    response = requests.get(f'http://offers/offers/get_offer/{id}')
    context = {'offer': response.json()['data']}
    return render(request, 'frontapp/offerDetail.html', context)


def login_view(request):
    return render(request, 'frontapp/login.html')


def new_offer_view(request):
    return render(request, 'frontapp/newOffer.html')


def room_view(request):
    return render(request, 'frontapp/room.html')
