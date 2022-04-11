from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

class CertificacionSerializer(serializers.ModelSerializer):
 class Meta:
        model = Certificacion
        fields = '__all__'

class AvaluadorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Avaluador
        fields = ['RNA', 'Nombre','Apellidos','Telefono','Celular','Ciudad','ConReg']
class AvaluadorDetailSerializer(serializers.ModelSerializer):
    Certificacion = CertificacionSerializer(many=True, read_only=True)
    class Meta:
        model = Avaluador
        fields = ['RNA', 'Nombre', 'Apellidos', 'Telefono','Celular','Ciudad','Titulo','Certificacion']
class CertificacionDirectorioSerializer(serializers.ModelSerializer):
    RNA = AvaluadorListSerializer( read_only=True)
    class Meta:
        model = Certificacion
        fields =  '__all__'