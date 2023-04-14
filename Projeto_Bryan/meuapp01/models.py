from django.db import models
from uuid import uuid4

# Create your models here.
class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=60, null=True)
    codigo = models.CharField(max_length=60, null=True)
    descricao = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.dados