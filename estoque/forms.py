UN_CHOICES = {
    "CX": "CX",
    "PÇ": "PÇ",
    "UN": "UN",
    "M": "M",
    "CM": "CM",
}

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
        widgets = {
            'unidade_compra': forms.Select(choices=UN_CHOICES),
            'unidade_requisicao': forms.Select(choices=UN_CHOICES),
        }
        exclude = ["id_material"]
