from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from .utils import *


class HotelHome(DataMixin, ListView):
    model = Apartaments
    template_name = 'touristapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'touristapp/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse('Обратная связь')


class ShowPost(DataMixin, DetailView):
    model = Apartaments
    template_name = 'touristapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class HotelCategory(DataMixin, ListView):
    model = Apartaments
    template_name = 'touristapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Apartaments.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
