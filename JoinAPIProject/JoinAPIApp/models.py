import datetime
import django
from django.db import models
from rest_framework.viewsets import ModelViewSet


# Create your models here.
class Cargo(models.Model):
    nome_cargo = models.CharField(unique=True)

    class Meta:
        db_table = 'cargo'


class Pessoa(models.Model):
    nome = models.CharField()
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column='id_cargo', related_name='pessoas')
    admissao = models.DateField(default=django.utils.timezone.now)

    class Meta:
        db_table = 'pessoa'


class Location(models.Model):
    nome = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_de_expiracao = models.DateField()

    class Meta:
        db_table = 'location'
