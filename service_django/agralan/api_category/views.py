from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)
from rest_framework.routers import DefaultRouter
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(
            CreateModelMixin, 
            UpdateModelMixin,
            DestroyModelMixin,
            ListModelMixin,
            GenericViewSet
        ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


router = DefaultRouter()
router.register('category', CategoryViewSet)