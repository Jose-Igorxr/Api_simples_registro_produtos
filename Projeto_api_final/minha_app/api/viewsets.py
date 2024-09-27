from rest_framework import viewsets, permissions
from minha_app.models import Nome, Produto, Categoria
from minha_app.api.serializers import NomeSerializer, ProdutoSerializer, CategoriaSerializer


class NomeViewSet(viewsets.ModelViewSet):
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
