from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse


def action_login(request):
    if request.is_ajax and request.method == "POST":
        response = requests.post('http://users/api/login', data=request.POST)
        if response.status_code == 200:
            request.session['logged_in'] = True
            request.session['user_id'] = response.json()['id']
            request.session['username'] = response.json()['username']

        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'wrong method'}, status=405)


def action_register(request):
    if request.is_ajax and request.method == "POST":
        response = requests.post('http://users/api/register', data=request.POST)
        if response.status_code == 200:
            request.session['logged_in'] = True
            request.session['user_id'] = response.json()['id']
            request.session['username'] = response.json()['username']

        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'wrong method'}, status=405)


def action_logout(request):
    request.session['logged_in'] = False
    return redirect('home_view')


def action_get_offers(request):
    if request.is_ajax and request.method == "GET":
        response = requests.get('http://offers/api/get_offers', params=request.GET)
        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'wrong method'}, status=405)


def action_add_offer(request):
    if request.is_ajax and request.method == "POST":
        response = requests.post('http://offers/api/add_offer', data=request.POST)
        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'wrong method'}, status=405)


def get_context_from_session(request):
    context = {'logged_in': request.session.get('logged_in'), 'user_id': request.session.get('user_id'),
               'username': request.session.get('username')}
    return context


def home_view(request):
    context = get_context_from_session(request)
    response = requests.get('http://offers/api/get_offers')
    context['offers'] = response.json()['data']
    return render(request, 'frontapp/home.html', context)


def offer_detail_view(request, id):
    context = get_context_from_session(request)
    response = requests.get(f'http://offers/api/get_offer/{id}')
    context['offer'] = response.json()['data']
    return render(request, 'frontapp/offerDetail.html', context)


def login_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/login.html', context)


def new_offer_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/newOffer.html', context)
