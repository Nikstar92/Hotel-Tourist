from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Главная страница')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Номера по категориям</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')