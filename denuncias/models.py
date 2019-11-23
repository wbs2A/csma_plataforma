from django.contrib.auth.models import User
from django.db import models


class Denuncia(models.Model):
    OP_ORIGEM = (('S', 'Sim'), ('N', 'Não'))
    STATUS_DENUNCIA = (("R", "Denúncia Registrada"), ("A", "Aguardando Resposta"), ("C", "Denúncia Concluída"), ("E", "Denúncia Excluída"))

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    status = models.CharField(max_length=1, choices=STATUS_DENUNCIA, default=STATUS_DENUNCIA[0][0])
    status_obs = models.TextField(default=STATUS_DENUNCIA[0][1])

    latitude = models.FloatField()
    longitude = models.FloatField()

    observacao = models.TextField()
    conhece_origem = models.CharField(max_length=1, choices=OP_ORIGEM)

    contato = models.CharField(max_length=30)

    def __str__(self):
        return self.observacao[:25]




