from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Apartaments.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'touristapp/index.html', context=context)


def about(request):
    return render(request, 'touristapp/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse('Обратная связь')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
