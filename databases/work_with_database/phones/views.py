from django.shortcuts import render
from phones.models import Phone


# При запросе <имя_сайта>/catalog/iphone-x - должна открываться страница с отображением информации по телефону.
# В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию (в алфавитном порядке) и
# по цене (по-убыванию и по-возрастанию).

def show_catalog(request):
    template = 'catalog.html'
    list_phones = Phone.objects.all()
    context = {
        'dict_phones': list_phones,
    }
    return render(request, template, context)


def show_product(request, phone_id):
    template = 'product.html'
    phone = Phone.objects.get(id=phone_id)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
