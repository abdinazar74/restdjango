from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import OrderingFilter, SearchFilter



class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'add_date']
    search_fields = ['product_name']
    permission_classes = [permissions.AllowAny]
