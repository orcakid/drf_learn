#from rest_framework import generics
from .models import Pers
from .serializers import PersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PersApiViews(APIView):
    
    
    def get(self, request):
        lst = Pers.objects.all()
        return Response({'champions': PersSerializer(lst, many=True).data})
    
    
    def post(self, request):
        serializer = PersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'pers': serializer.data})
    
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Update method not allowed'})
        
        try:
            pers = Pers.objects.get(pk=pk)
        except:
            return Response({'error': 'Pers does not exists'})
        
        seril = PersSerializer(data=request.data, instance=pers)
        seril.is_valid(raise_exception=True)
        seril.save()
        
        return Response({'new_pers': seril.data})
    
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Delete method not allowed'})
        
        try:
            pers = Pers.objects.get(pk=pk)
        except:
            return Response({'error': 'Pers not exists'})
        
        pers.delete()
        return Response({'succesfull': 'Pers was deleted'})