from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=50, default='Title')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    sections = models.ManyToManyField(Section, related_name='articles', through='SectionPosition')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class SectionPosition(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='positions')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')
