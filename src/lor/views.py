from .models import Pers, Сharacteristics
from .serializers import PersSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly


class PersViewSet(viewsets.ModelViewSet):
    queryset = Pers.objects.all()
    serializer_class = PersSerializer
    permission_classes = (IsAdminOrReadOnly, )
    
    
    @action(methods=['get'], detail=False)
    def classes_list(self, request):
        charact = Сharacteristics.objects.all()
        return Response({'all classes': {c.who: {'power':c.power, 'weapon': c.weapon, 'hp': c.hp} for c in charact}})
    
    





# class PersListCreateAPI(generics.ListCreateAPIView):
#     queryset = Pers.objects.all()
#     serializer_class = PersSerializer
    
    
# class PersUpdateAPI(generics.UpdateAPIView):
#     queryset = Pers.objects.all()
#     serializer_class = PersSerializer


# class PersCRUDapi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pers.objects.all()
#     serializer_class = PersSerializer

