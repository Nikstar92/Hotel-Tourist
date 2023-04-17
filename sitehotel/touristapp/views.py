from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Apartaments.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'touristapp/index.html', context=context)


def about(request):
    return render(request, 'touristapp/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse('Обратная связь')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = Apartaments.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) ==0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Апартаменты по категориям',
        'cat_selected': cat_id,
    }
    return render(request, 'touristapp/index.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
