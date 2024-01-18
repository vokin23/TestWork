from rest_framework import serializers
from .models import Letter, Parcel


class ParcelLetterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['sender_full_name',
                  'recipient_full_name',
                  'sending_point',
                  'receiving_point',
                  'sending_index',
                  'receiving_index']


class LetterSerializer(ParcelLetterSerializer):
    class Meta:
        model = Letter
        fields = ParcelLetterSerializer.Meta.fields + ['letter_type_choices', 'letter_type', 'letter_weight']


class ParcelSerializer(ParcelLetterSerializer):
    class Meta:
        model = Parcel
        fields = ParcelLetterSerializer.Meta.fields + ['notify_phone', 'parcel_type_choices', 'parcel_type', 'payment_amount']
