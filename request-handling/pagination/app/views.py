import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    df = pd.read_csv(
        r'C:\Users\tkaac\PycharmProjects\dj-homeworks-master\request-handling\pagination\data-398-2018-08-30.csv',
        encoding='cp1251')
    list = []
    nes_list = []
    for index, row in df.iterrows():
        d = row.to_dict()
        list.append(d)
    for i in list:
        nes_list.append({'Name': i['Name'], 'Street': i['Street'], 'District': i['District']})
    page_number = int(request.GET.get("page", 1))  # тут определяется параметр
    paginator = Paginator(nes_list, 10)  # используем пагинатор для разделения контента
    page = paginator.get_page(page_number)  # достаём одну страницу (которую запросили)
    context = {
        'page': page,
        'bus_stations': nes_list,  # как передать только те позиции, которые относятся к этой странице?
    }
    return render(request, 'index.html', context)
