from django.urls import path

from . import views

urlpatterns = [
    path("materiais/cadastro/", views.materiais_view, name="materiais_view"),
    path("tipos/cadastro/", views.tipos_view, name="tipos_view"),
]