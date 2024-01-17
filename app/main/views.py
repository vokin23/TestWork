from rest_framework import viewsets
from .models import Letter, Parcel
from .serializers import LetterSerializer, ParcelSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


