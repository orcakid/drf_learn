from rest_framework import generics
from .models import Pers
from .serializers import PersSerializer
from django.shortcuts import render
# Create your views here.

class PersApiViews(generics.ListAPIView):
    queryset = Pers.objects.all()
    serializer_class = PersSerializer