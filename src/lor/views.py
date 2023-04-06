#from rest_framework import generics
from .models import Pers
from rest_framework.views import APIView
from rest_framework.response import Response


class PersApiViews(APIView):
    def get(self, request):
        lst = Pers.objects.all().values()
        return Response({'champions': list(lst)})
    