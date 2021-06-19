from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea

from product.models import Product


class Reservation(models.Model):
    STATUS = (
        ('Beklemede', 'Beklemede'),
        ('Onaylandı', 'Onaylandı'),
        ('Reddedildi', 'Reddedildi'),
    )


    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservationdate = models.DateTimeField()
    stopdate = models.DateTimeField()
    total = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservationdate', 'stopdate']


# Create your models here.
