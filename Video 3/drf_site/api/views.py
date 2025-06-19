from django.shortcuts import get_object_or_404
from api.serializers import BarangSerializer
from api.models import Barang
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def barang_list(request):
    barangs = Barang.objects.all()
    serializer = BarangSerializer(barangs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def barang_detail(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    serializer = BarangSerializer(barang)
    return Response(serializer.data)
