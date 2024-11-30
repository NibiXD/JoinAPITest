from collections import defaultdict
from math import factorial
from typing import List, Dict

from django.core.exceptions import BadRequest
from django.core.serializers import serialize
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Location
from ..serializers import LocationSerializer

# Create your views here.
@api_view(['GET'])
def getMapTemplate(request):
    template = loader.get_template('mapTemplate.html')
    return HttpResponse(template.render())


@api_view(['GET'])
def getAllLocations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLocationById(request, id):
    location = Location.objects.get(id)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createLocation(request):
    serializer = LocationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest()

@api_view(['PUT'])
def updateLocation(request, id):
    location = Location.objects.get(id=id)
    serializer = LocationSerializer(instance=location, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest()


@api_view(['DELETE'])
def deleteLocation(request, id):
    location = Location.objects.get(id=id)
    location.delete()

    return Response('Local deletado')