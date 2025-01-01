from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Список Книг'
