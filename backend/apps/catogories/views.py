from django.shortcuts import render
from rest_framework import generics,filters
from .serializers import CategorySerializers
from .models import Category
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
   

