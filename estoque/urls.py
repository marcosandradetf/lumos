from django.urls import path

from . import views

urlpatterns = [
    path("materiais/cadastro/", views.cadastrar_materiais, name="cadastrar_materiais"),
    path("tipos/cadastro/", views.cadastrar_tipos_materiais, name="cadastrar_tipos_materiais"),
]