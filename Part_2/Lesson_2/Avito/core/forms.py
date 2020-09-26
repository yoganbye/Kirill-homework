from django import forms
from core.models import Ad, CategoriesAd

from django.core.exceptions import ValidationError


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        categories = forms.ModelChoiceField(
            queryset=CategoriesAd.objects.all(), empty_label=None, to_field_name = 'Категории'
        )
   
        fields = ['heading', 'categories', 'description', 'price', 'image']
        labels = {
            'heading' : 'Заголовок объявления',
            'categories' : 'Категория объявления',
            'description' : 'Описание объявления',
            'categories' : 'Категория объявления',
            'price' : 'Цена',
            'image' : 'Выберите файл',
        }
       
        widgets = {
            'heading' : forms.Textarea(attrs={
                'class' : 'form-control', 'placeholer' : 'Заголовок объявления'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control', 'placeholer' : 'Описание объявления'
            }),
            'price' : forms.Textarea(attrs={
                'class' : 'form-control', 'placeholer' : 'Цена'
            }),
            'image' : forms.ClearableFileInput(attrs={
                'type' : 'file', 'class' : 'form-control-file'
            }),
        }