from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse
import json


def action_login(request):
    if request.is_ajax and request.method == "POST":
        response = requests.post('http://host.docker.internal:8001/api/login', data=request.POST)
        if response.status_code == 200:
            request.session['username'] = request.POST['username']
            request.session['logged_in'] = True

        return JsonResponse(response.json(), status=response.status_code)


def action_register(request):
    if request.is_ajax and request.method == "POST":
        response = requests.post('http://host.docker.internal:8001/api/register', data=request.POST)
        if response.status_code == 200:
            request.session['username'] = request.POST['username']
            request.session['logged_in'] = True

        return JsonResponse(response.json(), status=response.status_code)


def action_add_product(request):
    response = requests.post('http://host.docker.internal:8001/api/products', data=request.POST)
    if response.status_code != 200:
        print("nieudane dodanie produktu") # todo show error in add offer page

    return redirect('home_view')


def action_logout(request):
    request.session['logged_in'] = False
    return redirect('home_view')


def get_context_from_session(request):
    context = {'username': request.session.get('username'), 'logged_in': request.session.get('logged_in')}
    return context

def home_view(request):
    context = get_context_from_session(request)
    response = requests.get('http://host.docker.internal:8001/api/products', data=request.GET)

    if response.status_code != 200:
        print("nieudane pobranie produktow") # todo show error in home page

    response_dict = json.loads(response.text)
    context['products'] = response_dict['data'];
    return render(request, 'frontapp/home.html', context)

def product_detail_view(request, id):
    context = get_context_from_session(request)
    response = requests.get(f'http://host.docker.internal:8001/api/products/{id}', data=request.GET)

    if response.status_code != 200:
        print("nieudane pobranie produktu") # todo show error in detail page

    response_dict = json.loads(response.text)
    context['product'] = response_dict['data'];
    return render(request, 'frontapp/productDetail.html', context)


def login_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/login.html', context)


def new_offer_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/newOffer.html', context)
