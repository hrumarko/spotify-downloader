from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class GetTitleForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'input-title form-control form-control-lg mt-5',
        'placeholder': 'Введите название трека и исполнителя',
        })
    )
    captcha = CaptchaField()
    
    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data.split(' ')) < 2:
            raise ValidationError('Введите и название и исполнителя трека для более точного поиска')
        return data
       
