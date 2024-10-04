# app_iluminacao/forms.py

from django import forms
from .models import Materiais, Categorias, Grupos, Tipos, Almoxarifados

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'

class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'

class TiposForm(forms.ModelForm):
    class Meta:
        model = Tipos
        fields = '__all__'

class AlmoxarifadosForm(forms.ModelForm):
    class Meta:
        model = Almoxarifados
        fields = '__all__'

class MateriaisForm(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = '__all__'
