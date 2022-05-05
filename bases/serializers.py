from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

class EmailSerializer(serializers.ModelSerializer):
 class Meta:
        model = Email
        fields = '__all__'

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
    Email = EmailSerializer(many=True, read_only=True)
    class Meta:
        model = Avaluador
        fields = ['RNA', 'Nombre', 'Apellidos', 'Telefono','Celular','Ciudad','Titulo','Certificacion','Email']
class CertificacionDirectorioSerializer(serializers.ModelSerializer):
    RNA = AvaluadorListSerializer( read_only=True)
    class Meta:
        model = Certificacion
        fields =  '__all__'
class CoordenadasListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Avaluador
        fields = ['RNA', 'Coordenadas']