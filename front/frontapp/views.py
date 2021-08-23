from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse


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


def action_logout(request):
    request.session['logged_in'] = False
    return redirect('home_view')


def get_context_from_session(request):
    context = {'username': request.session.get('username'), 'logged_in': request.session.get('logged_in')}
    return context


def home_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/home.html', context)


def login_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/login.html', context)


def new_offer_view(request):
    context = get_context_from_session(request)
    return render(request, 'frontapp/newOffer.html', context)
