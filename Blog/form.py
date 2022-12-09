from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from pprint import pprint
from .models import Comment

#Formulario de modal mensaje
class MessageForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['id', 'body']

   
   