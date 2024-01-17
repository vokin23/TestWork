from django.db import models


class Letters_parcels(models.Model):
    sender_full_name = models.CharField(max_length=100)
    recipient_full_name = models.CharField(max_length=100)
    sending_point = models.CharField(max_length=100)
    receiving_point = models.CharField(max_length=100)
    sending_index = models.IntegerField()
    receiving_index = models.IntegerField()

    def __str__(self):
        return f'{self.sender_full_name} - {self.recipient_full_name}'


class Letter(Letters_parcels):
    letter_type_choices = (
        (1, 'Common'),
        (2, 'Registered'),
        (3, 'Valuable'),
        (4, 'Express'),0
    )
    letter_type = models.IntegerField(choices=letter_type_choices)
    letter_weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'Letter'
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Parcel(Letters_parcels):
    notify_phone = models.CharField(max_length=20)
    parcel_type_choices = (
        (1, 'Small packet'),
        (2, 'Parcel'),
        (3, '1st class parcel'),
        (4, 'Valuable parcel'),
        (5, 'International parcel'),
        (6, 'Express parcel'),
    )
    parcel_type = models.IntegerField(choices=parcel_type_choices)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Parcel'
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'

