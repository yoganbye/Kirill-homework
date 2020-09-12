from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    pass


class Ad(models.Model):
    pass


class CategoriesAd(models.Model):
    pass

# 1. Реализовать модели, необходимые для реализации доски объявлений (подобной Avito).
#  Предлагаемая структура: У каждого “Пользователя” (у него есть 
# фото профиля и 
# дата рождения, помимо стандартной реализации) есть множество 
# “Объявлений” (Например:  “Продам гараж и.т.п.”, 
# обязательно есть заголовок, 
# описание и 
# фото), 
# которые 
#  разбиты по “Категориям” (Например: “Транспорт, недвижимость и.т.д.”)