from django.conf.urls import url
from django.urls import path, include

from advito import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    path('', views.page_one, name='page_one'),
]