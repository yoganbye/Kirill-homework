from django import forms
from core.models import Ad

from django.core.exceptions import ValidationError


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['heading', 'description', 'price', 'image']
        labels = {
            'heading' : 'Заголовок объявления',
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
            # 'categories' : forms.Select(attrs={
            #     'class' : 'form-control', 'placeholer' : 'Категория объявления', 'choices': 'sample'
            # }),
            'price' : forms.Textarea(attrs={
                'class' : 'form-control', 'placeholer' : 'Цена'
            }),
            'image' : forms.ClearableFileInput(attrs={
                'type' : 'file', 'class' : 'form-control-file'
            }),
        }