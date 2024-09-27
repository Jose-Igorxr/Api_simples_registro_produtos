from rest_framework import serializers
from minha_app.models import Nome, Categoria, Produto


class NomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nome
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
