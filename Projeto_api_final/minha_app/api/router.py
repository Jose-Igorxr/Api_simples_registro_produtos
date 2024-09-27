from minha_app.api import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'nome', viewsets.NomeViewSet, basename='nome')
router.register(r'produto', viewsets.ProdutoViewSet, basename='produto')
router.register(r'categoria', viewsets.CategoriaViewSet, basename='categoria')
