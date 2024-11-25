from rest_framework import serializers
from .models import *


class SALESerializer(serializers.ModelSerializer):
    class Meta:
        model=SALE
        fields='__all__'



class SALEApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SALE_Applications
        fields='__all__'