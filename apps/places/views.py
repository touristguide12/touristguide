from rest_framework import generics,filters
from .serializers import PlaceSerializer
from django.http import JsonResponse
from .models import Place
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name','description']
