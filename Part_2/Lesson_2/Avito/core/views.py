from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Profile, CategoriesAd, Ad



def index(request):
    '''
    Вьюха главной страницы
    '''
    announce_queryset = Ad.objects.all()
    # response = ['id:{}|description:{}|time:{}\n'.format(announce.id, announce.description, announce.date_pub)\
    #      for announce in announce_queryset]
    template = loader.get_template('core/index.html')
    context = {
        'posts' : announce_queryset
    }
    return HttpResponse(template.render(context))
    

def announce(request):
    '''
    Вьюха страницы со всеми объявлениями
    '''
    return HttpResponse('Все объявления')


def det_announce(request, announce_id):
    '''
    Вьюха детального представления объявления
    '''
    announce = Ad.objects.get(id=announce_id)
    response = 'Детальное представление объявления №{}\
        Author:{}| description:{}'.format(announce_id, announce.author, announce.description)
    return HttpResponse(response)


def categories(request):
    '''
    Вьюха страницы с разделением по категориям
    '''
    return HttpResponse('Страница с разделением по категориям')


def ad_edit(request, announce_id):
    '''
    Вьюха редактирования объяления
    '''
    response = 'Редактирование объявления №{}'.format(announce_id)
    return HttpResponse(response)


def ad_create(request, announce_id):
    '''
    Вьюха создания объявления
    '''
    response = 'Создание объявления №{}'.format(announce_id)
    return HttpResponse(response)


def ad_delete(request, announce_id):
    '''
    Вьюха удаления объявления
    '''
    response = 'Удаление объявления объявления №{}'.format(announce_id)
    return HttpResponse(response)