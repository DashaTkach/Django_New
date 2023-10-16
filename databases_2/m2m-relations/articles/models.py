from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):
    # name = models.CharField(max_length=50, default='Title')
    # articles = models.ManyToManyField(Article, related_name='sections')
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class SectionPosition(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='positions')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')

    # удалить и заново создать базу
    # 1 - разобраться с through = узнать, как представить разделы
    # 2 - настроить отображение ярлыков
