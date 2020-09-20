from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('announcement/', views.announce, name='announce'),
    path('announcement/<int:announce_id>/', views.det_announce, name='det_announce'),
    path('announcement/<int:announce_id>/create/', views.ad_create, name='ad_create'),
    path('announcement/<int:announce_id>/edit/', views.ad_edit, name='ad_edit'),
    path('announcement/<int:announce_id>/delete/', views.ad_delete, name='ad_delete'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:categories_id>/', views.det_categories, name='det_categories'),
]