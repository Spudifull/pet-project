# -*- coding: utf-8 -*

from django.shortcuts import render
from django.shortcuts import redirect
from Frontend.settings import FASTAPI_SERVER_URL
import requests
def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')

    error_message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.post(
            f'{FASTAPI_SERVER_URL}/users/login',
            data={'username': username, 'password': password},
            timeout=5
        )

        if response.status_code == 200:
            request.session['access_token'] = response.json().get('access_token')
            return redirect('private_office')
        else:
            error_message = "Неверный адрес электронной почты или пароль"

    return render(request, 'login.html', {'error': error_message})

def password_reset(request):
    pass


def password_register(request):
    pass


def create_polls(request):
    return render(request, 'create_polls.html')


def create_survey(request):
    pass


def private_office(request):
    return render(request, 'private_office.html')


def my_surveys(request):
    pass


def profile(request):
    pass


def settings(request):
    pass


def faq(request):
    return render(request, 'faq.html')

