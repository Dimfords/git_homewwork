from django import forms
from .models import warehouseadapp
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# from django.contrib.auth.forms import AuthenticationForm

# class UserLoginForm(AuthenticationForm):
#     username  = forms.CharField(label='Max 150')
#     password  = forms.CharField(label='Max 150')

class AddBB(forms.Form):
    title = forms.CharField(max_length=150, label='Название')
    content = forms.CharField(label='Контент', required=False)
    is_published = forms.BooleanField(label='Опубликовано')
    photo = forms.ImageField()


class Test_add_BB(forms.ModelForm):
    class Meta:
        model = warehouseadapp
        fields = ('title','content','qr_decode')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Привет!', 'disabled':'disabled', 'id':'decoded'}),
            'content': forms.TextInput(attrs={'class': 'form-control','required pattern': '^([0-1]?[\d][\d][\d])$'}),
            'qr_decode': forms.Select(attrs={'class': 'form-control'}),
        }


class scan_qr_form(forms.ModelForm):
    title = forms.CharField(label='Наименование', widget = forms.TextInput(attrs={'placeholder':'Тут будет код', \
        'id':'decoded', 'readonly':'readonly'}))
    qr_decode = forms.CharField(label='Вес, кг', widget = forms.TextInput(attrs={'autofocus':'autofocus',\
        'autocomplete':'off','placeholder':'Отсканируйте qr-код', 'required pattern': '^([0-1]?[\d][\d][\d])$',\
            'inputmode':'numeric'\
        }))
    user = forms.CharField(label='Користувач', widget = forms.TextInput(attrs={'value':'{{ request.user.first_name}}'}))

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Надіслати', css_class='btn-primary'))
    helper.form_method = 'POST'
   
    class Meta:
        model = warehouseadapp
        fields = ['title','qr_decode']
       

    # def clean_qr_decode(self):
    #     qr_decode = self.cleaned_data['qr_decode']
    #     if not '777' in qr_decode:
    #         raise forms.ValidationError('Это не уникальный номер биг-бега!')
    #     else:
    #         return qr_decode
    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy('scan_qr')
    #     self.helper.form_method = 'POST'
    #     self.helper.form_id = 'scan_qr_form'
    #     self.helper.attrs = {
    #         'hx-post': reverse_lazy('scan_qr'),
    #         'hx-target': '#scan_qr_form',
    #         'hx-swap': 'outerHTML'
    #     }
    #     self.helper.add_input(Submit('submit', 'Send'))
        

    


# class scan_qr_form(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         # self.helper.form_action = reverse_lazy('scan_qr')
#         # self.helper.form_method = 'GET'
#         self.helper.form_id = 'scan_qr_form'
#         self.helper.attrs = {
#             'hx-post': reverse_lazy('scan_qr'),
#             'hx-target': '#scan_qr_form',
#             'hx-swap': 'outerHTML'
#         }
#         self.helper.add_input(Submit('submit', 'Send'))
        

#     CHOICES = (
#         ('CORN', 'CORN'),
#         ('SF', 'SF'),
#         ('SOYBEAN', 'SOYBEAN'),
#     )

#     class Meta:
#         model = warehouseadapp
#         fields = ('qr_decode', 'crop')
        
    
#     def clean_qr_decode(self):
#         qr_decode_field = self.cleaned_data['qr_decode']
#         if len(qr_decode_field) <= 3:
#             raise forms.ValidationError("Username is too short")
#         return qr_decode


