from django.contrib.auth.models import User
from django.db import models


class LotSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название раздела')
    description = models.TextField(max_length=500, verbose_name='Описание раздела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'


class Lot(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название лота')
    description = models.TextField(max_length=500, verbose_name='Описание лота')
    section = models.ForeignKey(LotSection, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Раздел')
    is_sold = models.BooleanField(verbose_name='Продано', default=False)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    starting_price = models.FloatField(verbose_name='Начальная цена', default=0)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='lots_images', blank=True, verbose_name='Фото лота')
    favorites = models.ManyToManyField(User, related_name='favorites')
    highest_price = models.FloatField(verbose_name='Наибольшая цена', default=0)
    current_buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='competition_lots')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lots'
        verbose_name = 'лот'
        verbose_name_plural = 'лоты'
        permissions = [('can_mark_as_suspicious', 'Может помечать как подозрительное')]


class LotComment(models.Model):
    lot_binding = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Комментарий', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(verbose_name='Текст комментария')
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

# class LotImage(models.Model):
#     lot_binding = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Лот')
#     image = models.ImageField(upload_to='lots_images', blank=True, verbose_name='Фото лота')
