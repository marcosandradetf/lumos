from django.urls import path

from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar_materiais, name="cadastrar_materiais"),
]