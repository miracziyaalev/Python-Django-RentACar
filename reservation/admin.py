from django.contrib import admin

from home.models import Setting, ContactFormMessage, UserProfile
from reservation.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rezdate', 'returndate', 'note', 'status']
    list_filter = ['status']





admin.site.register(Reservation, ReservationAdmin)
