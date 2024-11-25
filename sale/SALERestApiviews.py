
from django.shortcuts import render
from rest_framework import generics,viewsets,status

from sale.serializers import SALESerializer,SALEApplicationsSerializer
from .models import *
from rest_framework.response import Response




class SALEViewsets(viewsets.ModelViewSet):
    queryset=SALE.objects.all()
    serializer_class=SALESerializer

    

    def getByRegisterId(self,request,register_id):
     try:
        queryset = SALE.objects.filter(dsa_registerid=register_id)
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data,status=200)
        else:
            return Response({"message": "No records found"}, status=404)
     except Exception as e:
        return Response({"error": str(e)}, status=500)


class SALE_AppliViewsets(viewsets.ModelViewSet):
    queryset=SALE_Applications.objects.all()
    serializer_class=SALEApplicationsSerializer

   

   