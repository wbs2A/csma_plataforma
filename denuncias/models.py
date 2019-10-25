from django.db import models

class Denuncia(models.Model):
    op_origem = (('S', 'Sim'), ('N', 'Não'))
    latitude = models.FloatField()
    longitude = models.FloatField()
    observacao = models.TextField()
    conhece_origem = models.CharField(max_length=1, choices=op_origem)
    contato = models.CharField(max_length=30)





