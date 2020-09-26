from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .forms import AdForm

from .models import Profile, CategoriesAd, Ad


def index(request):
    '''
    Вьюха главной страницы
    '''
    announce_queryset = Ad.objects.all().order_by('-date_pub')[:7]
    context = {
        'posts' : announce_queryset,
    }
    return render(request, 'core/index.html', context)


def det_announce(request, announce_id):
    '''
    Вьюха детального представления объявления
    '''
    try:
        announce = Ad.objects.get(id=announce_id)  
        announce.views_count += 1
        announce.save()
    except Ad.DoesNotExist:
        raise Http404("Post does not exist")
    context = {
        'announce' : announce
    }
    return render(request, 'core/det_announce.html', context)


def announce(request):
    '''
    Вьюха страницы со всеми объявлениями
    '''
    announce_queryset = Ad.objects.all().order_by('-date_pub')
    context = {
        'posts' : announce_queryset,
    }
    return render(request, 'core/announce.html', context)


def categories(request):
    '''
    Вьюха страницы с разделением по категориям
    '''
    categories_queryset = CategoriesAd.objects.all()
    context = {
        'categories' : categories_queryset
    }
    return render(request, 'core/categories.html', context)


def det_categories(request, categories_id):
    cat = CategoriesAd.objects.get(id=categories_id)
    det_categories_queryset = Ad.objects.filter(categories = cat)
    context = {
        'det_categories' : det_categories_queryset,
        'cat' : cat,
    }
    return render(request, 'core/det_categories.html', context)
    

def ad_edit(request, announce_id):
    '''
    Вьюха редактирования объяления
    '''
    response = 'Редактирование объявления №{}'.format(announce_id)
    return HttpResponse(response)


def ad_create(request):
    '''
    Вьюха создания объявления
    '''
    form = AdForm()
    template_name = 'core/ad_create.html'
    context = {'form' : form}

    if request.method == "GET":
        return render(request, template_name, context)
    elif request.method == "POST":
        form = AdForm(request.POST, request.FILES)

        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            context['ad_was_created'] = True
            return render(request, template_name, context)
        else:
            context['ad_was_created'] = False
            context['form'] = form
            return render(request, template_name, context)


def ad_delete(request, announce_id):
    '''
    Вьюха удаления объявления
    '''
    response = 'Удаление объявления объявления №{}'.format(announce_id)
    return HttpResponse(response)


