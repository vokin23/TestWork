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
    LETTER_TYPE_CHOICES = (
        (1, 'Common'),
        (2, 'Registered'),
        (3, 'Valuable'),
        (4, 'Express'),
    )
    LETTER_TYPE = models.IntegerField(choices=LETTER_TYPE_CHOICES)
    LETTER_WEIGHT = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'product'
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
        db_table = 'product'
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_image', blank=True, null=True, verbose_name='Изоображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
