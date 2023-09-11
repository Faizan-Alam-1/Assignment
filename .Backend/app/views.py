from django.shortcuts import render
from django.http import HttpResponse
import json
from app.models import EnergyData
from .serializers import EnergyDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def energy_data_list(request):
    data = EnergyData.objects.all()
    serializer = EnergyDataSerializer(data, many=True)
    return Response(serializer.data)





