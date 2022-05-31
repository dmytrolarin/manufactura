from django.db import models
from django.urls import reverse

# Модель для блюд
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Страва')
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name='URL страви')
    composition = models.TextField(blank=True, verbose_name='Склад')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/",verbose_name='Фото')
    price = models.IntegerField(verbose_name='Ціна')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True, verbose_name='Категорія страви')

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

    def __str__(self):
        return self.name

# Модель для категорий блюд
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,verbose_name='Категорія страви')
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name='URL категорії')

    class Meta:
        verbose_name = 'Категорія страви'
        verbose_name_plural = 'Категорії страв'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug':self.slug})


