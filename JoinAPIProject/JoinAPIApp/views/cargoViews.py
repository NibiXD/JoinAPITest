from django.core.exceptions import BadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Cargo
from ..serializers import CargoSerializer

# Create your views here.
#Cargo
@api_view(['GET'])
def getAllCargos(request):
    cargos = Cargo.objects.all()
    serializer = CargoSerializer(cargos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCargoById(request, id):
    cargo = Cargo.objects.get(id=id)
    serializer = CargoSerializer(cargo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addCargo(request):
    serializer = CargoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest


@api_view(['PUT'])
def updateCargo(request, id):
    cargo = Cargo.objects.get(id=id)
    serializer = CargoSerializer(instance=cargo, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return BadRequest()


@api_view(['DELETE'])
def deleteCargo(request, id):
    cargo = Cargo.objects.get()
    cargo.delete()

    return Response('Cargo deletado!')