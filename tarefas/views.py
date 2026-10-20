from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Tarefa
from .forms import CadastroForm, TarefaForm


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("lista_tarefas")
    else:
        form = CadastroForm()

    return render(request, "tarefas/cadastro.html", {
        "form": form
    })


@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(
        usuario=request.user
    ).order_by("-data_criacao")

    return render(request, "tarefas/lista.html", {
        "tarefas": tarefas
    })


@login_required
def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()

            messages.success(request, "Tarefa criada com sucesso!")
            return redirect("lista_tarefas")
    else:
        form = TarefaForm()

    return render(request, "tarefas/formulario.html", {
        "form": form,
        "titulo": "Nova tarefa"
    })


@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(
        Tarefa,
        pk=pk,
        usuario=request.user
    )

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada!")
            return redirect("lista_tarefas")
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, "tarefas/formulario.html", {
        "form": form,
        "titulo": "Editar tarefa"
    })


@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(
        Tarefa,
        pk=pk,
        usuario=request.user
    )

    if request.method == "POST":
        tarefa.delete()
        messages.success(request, "Tarefa excluída!")
        return redirect("lista_tarefas")

    return render(request, "tarefas/confirmar_exclusao.html", {
        "tarefa": tarefa
    })