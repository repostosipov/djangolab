from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def ads_count(self):
        return Ads.objects.filter(seller=self).count()

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тэга")

    def __str__(self):
        return self.title


class Ads(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    text = models.TextField(null=True, blank=True,
                            verbose_name="текст объявления")
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, verbose_name="продавец")
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name="категория объявления")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        'Tag', verbose_name="тэги")
    price = models.PositiveIntegerField(verbose_name="цена")

    def __str__(self):
        return self.title
