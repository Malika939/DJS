from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField('Текст', blank=True)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата обновления', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField('Опубликовано', default=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


