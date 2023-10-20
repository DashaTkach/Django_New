from django.contrib import admin

from .models import Article, SectionPosition, Section


class SectionPositionInLine(admin.TabularInline):
    model = SectionPosition
    extra = 5


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    list_filter = ['published_at']
    inlines = [SectionPositionInLine, ]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', ]
