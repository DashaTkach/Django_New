from collections import Counter

from django.shortcuts import render


# подсчет переходов с лендинга
def index(request):
    from_landing = request.GET.get("from-landing")

    if from_landing == 'original':
        counter_click_original = Counter()

    elif from_landing == 'test':
        counter_click_test = Counter()

    return render(request, 'index.html')


# раздельный показ двух разных страниц
def landing(request):
    way_of_view = request.GET.get("ab-test-arg")
    if way_of_view == 'original':
        counter_show_original = Counter()
        return render(request, 'landing.html')

    elif way_of_view == 'test':
        counter_show_test = Counter()
        return render(request, 'landing_alternate.html')

# вывод отношения количества переходов к количеству показов страницы
def stats(request):
    return render(request, 'stats.html', context={
        'test_conversion': 0.5,
        'original_conversion': 0.4,
    })


# а как в таком случае сделать подсчёт, если он тут и так считает эти числа???