from rest_framework import serializers
from .models import Letter, Parcel


class ParcelLetterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class LetterSerializer(ParcelLetterSerializer):
    class Meta:
        model = Letter


class ParcelSerializer(ParcelLetterSerializer):
    class Meta:
        model = Parcel
