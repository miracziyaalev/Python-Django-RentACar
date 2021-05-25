from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea

from product.models import Product


class Reservation(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rezdate = models.CharField(max_length=50)
    reztime = models.CharField(max_length=200)
    returndate = models.CharField(max_length=50)
    returntime = models.CharField(max_length=200)



    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title


class ReservationFormu(ModelForm):
    class Meta:
        model = Reservation
        fields = ['rezdate', 'reztime', 'returndate', 'returntime']


# Create your models here.
