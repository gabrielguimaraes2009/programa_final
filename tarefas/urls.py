from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.lista_tarefas, name="lista_tarefas"),
    path("cadastro/", views.cadastro, name="cadastro"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="tarefas/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    path("criar/", views.criar_tarefa, name="criar_tarefa"),
    path("editar/<int:pk>/", views.editar_tarefa, name="editar_tarefa"),
    path("excluir/<int:pk>/", views.excluir_tarefa, name="excluir_tarefa"),
]