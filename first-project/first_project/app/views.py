import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

#  здесь мы прописали содержание того, что будет отражено на сайте

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir = os.listdir(path=r'C:\Users\tkaac\PycharmProjects\dj-homeworks\1.1-first-project')
    msg = f'Рабочая директория: {workdir}'
    return HttpResponse(msg)
