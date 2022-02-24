from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
from django import forms
from dateutil.relativedelta import relativedelta

class CertificacionCreateForm(ModelForm):
    class Meta:
        model = Certificacion
        fields = ['Categoria', 'RNA', 'Otorgamiento', 'Renovacion','Vigencia']
        #Todo para calculos automaticos
    def save(self, commit=True):
        model = super(ModelForm, self).save(commit=False)
        model.PrimerVencimiento = model.Otorgamiento + relativedelta(years= model.Vigencia)
        if model.Renovacion:
            model.Vencimiento = model.Renovacion + relativedelta(years= model.Vigencia)
        results = Certificacion.objects.filter(Categoria = model.Categoria).order_by('Codigo').last()
        numero = int(results.Codigo.split('-')[1]) + 1
        model.Codigo = model.Categoria + '-' + str(numero) 
        return model

class SearchForm(forms.Form):
    matricula = forms.CharField(label='Matricula', max_length=100,required=False)
    nombre = forms.CharField(label='Nombre', max_length=100,required=False)
    apellidos = forms.CharField(label='Apellidos', max_length=100,required=False)