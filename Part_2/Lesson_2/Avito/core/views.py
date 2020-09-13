from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def announce(request):
    return HttpResponse('Все объявления')


def det_announce(request, announce_id):
    response = 'Детальное представление объявления №{}'.format(announce_id)
    return HttpResponse(response)


def categories(request):
    return HttpResponse('Страница с разделением по категориям')


def ad_edit(request, announce_id):
    response = 'Редактирование объявления №{}'.format(announce_id)
    return HttpResponse(response)


def ad_create(request, announce_id):
    response = 'Создание объявления №{}'.format(announce_id)
    return HttpResponse(response)


def ad_delete(request, announce_id):
    response = 'Удаление объявления объявления №{}'.format(announce_id)
    return HttpResponse(response)