from django.shortcuts import redirect, render
import requests


def action_login(request):
    response = requests.post('http://127.0.0.1:8001/api/login', data=request.POST)
    if response.status_code != 200:
        print("nieudane logowanie") # todo show error in login page
        return redirect('home_view')

    request.session['username'] = request.POST['username']
    request.session['logged_in'] = True
    return redirect('home_view')


def action_register(request):
    response = requests.post('http://127.0.0.1:8001/api/register', data=request.POST)
    if response.status_code != 200:
        print("nieudana rejestracja") # todo show error in login page
        return redirect('home_view')

    request.session['username'] = request.POST['username']
    request.session['logged_in'] = True
    return redirect('home_view')


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
