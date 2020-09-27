from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('announcement/', views.announce, name='announce'),

    path('announcement/<int:announce_id>/', views.AnnounceView.as_view(), name='det_announce'),

    path('announcement/create/', views.CreateAdView.as_view(), name='ad_create'),

    path('announcement/<int:announce_id>/edit/', views.EditeAdView.as_view(), name='ad_edit'),
    
    path('announcement/<int:announce_id>/delete/', views.DeleteAdView.as_view(), name='ad_delete'),

    path('announcement/<int:announce_id>/delete_success/', TemplateView.as_view(
        template_name='core/delete_success.html'), name='delete_ad_success'
    ),
    path('categories/', views.categories, name='categories'),

    path('categories/<int:categories_id>/', views.det_categories, name='det_categories'),
]