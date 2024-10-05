from django.urls import path

from . import views

urlpatterns = [
    # materiais
    path("materiais/cadastro/", views.view_material, name="view_material"),
    path("materiais/delete/<int:id>/", views.delete_material, name="delete_material"),
    path("materiais/update/<int:id>/", views.update_material, name="update_material"),

    # tipos
    path("tipos/cadastro/", views.view_tipos, name="view_tipos"),

]