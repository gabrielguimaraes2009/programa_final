from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ("Pendente", "Pendente"),
        ("Em andamento", "Em andamento"),
        ("Concluída", "Concluída"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pendente"
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo