from rest_framework import serializers
from .models import Pessoa, Cargo, Location


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer(source='id_cargo')

    class Meta:
        model = Pessoa
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class Question4PessoaSerializer(serializers.ModelSerializer):
    cargo = serializers.CharField(source='id_cargo.nome_cargo')

    class Meta:
        model = Pessoa
        fields = ['nome', 'cargo', 'admissao']


class Question4CargoSerializer(serializers.ModelSerializer):
    total_funcionarios = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cargo
        fields = '__all__'