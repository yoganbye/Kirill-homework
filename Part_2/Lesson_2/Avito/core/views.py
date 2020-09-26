from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .forms import AdForm
from django.views.generic import ListView, View, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .exceptions import PermissionDenied
from .models import Profile, CategoriesAd, Ad


class IndexView(ListView):
    '''
    Вьюха главной страницы
    '''
    model = Ad
    template_name = 'core/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Ad.objects.all().order_by('-date_pub')[:7]


class CreateAdView(CreateView):
    '''
    Вьюха создания объявления
    '''
    form_class = AdForm
    template_name = 'core/ad_create.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}

        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            context['ad_was_created'] = True
            context['form'] = self.form_class
            return render(request, self.template_name, context)
        else:
            context['ad_was_created'] = False
            context['form'] = form
            return render(request, template_name, context)


class DeleteAdView(DeleteView):
    """
    Вьюха удаления объявления
    """
    model = Ad
    pk_url_kwarg = 'announce_id'
    template_name = 'core/ad_delete.html'

    def get_success_url(self):
        announce_id = self.kwargs['announce_id']
        return reverse('delete_ad_success', args=(announce_id, ))


class EditeAdView(UpdateView):
    """
    Вьюха редактирования объявления
    """
    model = Ad
    pk_url_kwarg = 'announce_id'
    template_name='core/ad_edit.html'
    form_class = AdForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("You are not author of this post")
        return super(EditeAdView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        announce_id = self.kwargs['announce_id']
        return reverse('det_announce', args=(announce_id, ))


class AnnounceView(View):
    '''
    Вьюха детального представления объявления
    '''
    template_name = 'core/det_announce.html'

    def get(self, request, announce_id, *args, **kwargs):
        try:
            announce = Ad.objects.get(id=announce_id)  
            announce.views_count += 1
            announce.save()
        except Ad.DoesNotExist:
            raise Http404("Post does not exist")
        context = {
            'announce' : announce
        }
        return render(request, self.template_name, context)


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
    """
    Вьюха с оюъявлениями из одной категории
    """
    cat = CategoriesAd.objects.get(id=categories_id)
    det_categories_queryset = Ad.objects.filter(categories = cat)
    context = {
        'det_categories' : det_categories_queryset,
        'cat' : cat,
    }
    return render(request, 'core/det_categories.html', context)


# def index(request):
#     '''
#     Вьюха главной страницы
#     '''
#     announce_queryset = Ad.objects.all().order_by('-date_pub')[:7]
#     context = {
#         'posts' : announce_queryset,
#     }
#     return render(request, 'core/index.html', context)


# def ad_create(request):
#     '''
#     Вьюха создания объявления
#     '''
#     form = AdForm()
#     template_name = 'core/ad_create.html'
#     context = {'form' : form}

#     if request.method == "GET":
#         return render(request, template_name, context)
#     elif request.method == "POST":
#         form = AdForm(request.POST, request.FILES)

#         if form.is_valid():
#             ad = form.save(commit=False)
#             ad.author = request.user
#             ad.save()
#             context['ad_was_created'] = True
#             return render(request, template_name, context)
#         else:
#             context['ad_was_created'] = False
#             context['form'] = form
#             return render(request, template_name, context)


# def det_announce(request, announce_id):
#     '''
#     Вьюха детального представления объявления
#     '''
#     try:
#         announce = Ad.objects.get(id=announce_id)  
#         announce.views_count += 1
#         announce.save()
#     except Ad.DoesNotExist:
#         raise Http404("Post does not exist")
#     context = {
#         'announce' : announce
#     }
#     return render(request, 'core/det_announce.html', context)


