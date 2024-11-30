from collections import defaultdict
from math import factorial
from typing import List, Dict

from django.core.exceptions import BadRequest
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Pessoa, Cargo
from ..serializers import *

# Create your views here.

#Pessoas
@api_view(['GET'])
def getAllPessoas(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPessoaById(request, id):
    pessoa = Pessoa.objects.get(id=id)
    serializer = PessoaSerializer(pessoa, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addPessoa(request):
    serializer = PessoaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest

@api_view(['PUT'])
def updatePessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    serializer = PessoaSerializer(instance=pessoa, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest()


@api_view(['DELETE'])
def deletePessoa(request, id):
    pessoa = Pessoa.objects.get()
    pessoa.delete()

    return Response('Pessoa deletada!')


#Exercícios
@api_view(['GET'])
def question1(request):
    list = [9, 2, 95, 28, 0, 73, 81, 91, 71, '22', 6, 21, 1, 47, "52", 35, 68, 29, 66, 91, 81, "99", 40]
    [sorted_list, minValue, maxValue] = redoList(list)
    return HttpResponse(f'lista ordenada: {sorted_list} <br> menor valor: {minValue} <br> maior valor: {maxValue}')


@api_view(['GET'])
def question2(request, value):
    result = factorial(value)
    return HttpResponse(f'Fatorial de {value}: {result}')


@api_view(['GET'])
def question3(request):
    objectRequest = [
        {
            "message_tag": "TEMPERATURE_MIN",
            "element_dictionary": "INMET",
            "element": "MIN_AIR_TEMP_2M_C"
        },
        {
            "message_tag": "RELATIVE_HUMIDITY_MIN",
            "element_dictionary": "INMET",
            "element": "MIN_REL_HUMIDITY_2M_PCT"
        },
        {
            "message_tag": "temperature",
            "element": "AVG_AIR_TEMP_2M_C",
            "element_dictionary": "METAR"
        },
        {
            "message_tag": "PrecMin",
            "element_dictionary": "SIMEPAR_MET",
            "element": "DISCARDED",
        },
        {
            "message_tag": "Prec",
            "element_dictionary": "SIMEPAR_MET",
            "element": "ACCUM_PRECIP_2M_MM",
        }
    ]
    result = organizeObject(objectRequest)
    return Response(result)

@api_view(['GET'])
def question4a(request):
    pessoas = Pessoa.objects.all().select_related('id_cargo').order_by('admissao')
    serializer = Question4PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def question4b(request):
    pessoas = Pessoa.objects.all().select_related('id_cargo').order_by('admissao')[:1]
    serializer = Question4PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def question4c(request):
    cargos = Cargo.objects.annotate(total_funcionarios=Count('pessoas')).filter(total_funcionarios__gt=0)
    serializer = Question4CargoSerializer(cargos, many=True)
    return Response(serializer.data)


def redoList(list: List):
    numericValues = [int(item) for item in list]
    reverseValues = sorted(numericValues, reverse=True)
    minValue = min(reverseValues)
    maxValue = max(reverseValues)
    return reverseValues, minValue, maxValue


def organizeObject(objectRequest: list):
    groupedDict = defaultdict(list)

    for item in objectRequest:
        dictionary = item["element_dictionary"]
        element = item["element"]
        groupedDict[dictionary].append(element)

    return [dict(groupedDict)]