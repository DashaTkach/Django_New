from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Section


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    scopes = Section.objects.all()
    context = {
        'object_list': object_list,
        'scopes': scopes,
    }
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    return render(request, template, context)


# как настроить отображение ярлыков?
# нужно делать отдельное поле в таблице?