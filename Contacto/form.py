from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from pprint import pprint

#Formulario de la pagina contacto
class Formulario(forms.Form):

    name = forms.CharField(label="nombre:", required=True, widget=forms.TextInput)
    email = forms.EmailField(label="email:", required=True)
    content = forms.CharField(label="Contenido:", widget=forms.Textarea)
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contacto')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('enviar', 'Enviar'))