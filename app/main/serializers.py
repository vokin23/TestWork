from rest_framework import serializers
from .models import Letter, Parcel


class Parcel_LetterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class LetterSerializer(Parcel_LetterSerializer):
    class Meta:
        model = Letter


class ParcelSerializer(Parcel_LetterSerializer):
    class Meta:
        model = Parcel
