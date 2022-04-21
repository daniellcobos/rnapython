from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
from django import forms
from dateutil.relativedelta import relativedelta

class CertificacionCreateForm(ModelForm):
    class Meta:
        model = Certificacion
        fields = ['Categoria', 'RNA', 'Otorgamiento', 'Renovacion','VigenciaOtorgamiento','VigenciaRenovacion']
        #Todo para calculos automaticos
    def save(self, commit=True):
        model = super(ModelForm, self).save(commit=False)
        model.PrimerVencimiento = model.Otorgamiento + relativedelta(years= model.VigenciaOtorgamiento)
        if model.Renovacion:
            model.Vencimiento = model.Renovacion + relativedelta(years= model.VigenciaRenovacion)
        results = Certificacion.objects.filter(Categoria = model.Categoria).order_by('Codigo').last()
        numero = int(results.Codigo.split('-')[1]) + 1
        model.Codigo = model.Categoria + '-' + str(numero) 
        return model

class SearchForm(forms.Form):
    matricula = forms.CharField(label='Matricula', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    identificacion = forms.CharField(label='Identificacion', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

class SearchVigForm(forms.Form):
    CHOICESVig=[('Vigentes','Vigentes'),
         ('Vencidos','Vencidos')]
    Categoria_CHOICES = [
    ( 'URB', 'Urbano'),
    ('RUR', 'Rural'),
    ('ESP', 'Especiales'),
    ('MYE', 'Maquinaria y Equipo'),
    ]
    Vigente = forms.ChoiceField(choices=CHOICESVig, widget=forms.RadioSelect)
    Categoria = forms.ChoiceField(choices=Categoria_CHOICES, widget=forms.RadioSelect)
   