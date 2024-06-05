from rest_framework import generics
from .models import Moto, Fabricante
from .serializers import MotoSerializer, FabricanteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Clases genericas para el modelo de moto
class MotoList(generics.ListCreateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
class InfoMoto(generics.RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
class MotoUpdate(generics.UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
class MotoDelete(generics.DestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
# Clases genericas para el modelo de fabricante
class FabricanteList(generics.ListCreateAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    
class InfoFabricante(generics.RetrieveAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    
class FabricanteUpdate(generics.UpdateAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    
class FabricanteDelete(generics.DestroyAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    

# Vista personalizada
@api_view(['GET'])
def motos_fabricante(request, fabricante_id):
    moto = Moto.objects.filter(fabricante_id=fabricante_id)
    serializer = MotoSerializer(moto, many=True)
    return Response(serializer.data)

