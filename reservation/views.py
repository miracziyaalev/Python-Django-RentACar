from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import product
from product import models
from product.models import Product
from reservation.models import ReservationForm, Reservation


def index(request):
    return HttpResponse("Reserve Page")



@login_required(login_url="/login")
def sendreserve(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    total = 1

    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = Reservation()  # create relation with model
            data.reservationdate = form.cleaned_data['reservationdate']
            data.stopdate = form.cleaned_data['stopdate']
            delta = form.cleaned_data['stopdate'] - form.cleaned_data['reservationdate']
            days = delta.days
            if delta.seconds > 0:
                days = delta.days + 1

            if delta.days < 0:
                messages.error(request, "Lütfen tarih aralığını doğru seçiniz...")
                return HttpResponseRedirect(url)


            data.ip = request.META.get('REMOTE_ADDR')
            data.total = total * Product.objects.get(id=id).price * days
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id

            amount = Product.objects.get(id=id).amount

            if amount > 0:
                product = Product.objects.get(id=id)
                product.amount = product.amount -1
                product.save()

                data.save() # save data to table

            else:
                messages.error(request, "Bu modele ait tüm araçlarımız kullanımdadır.")
                return HttpResponseRedirect(url)

            messages.success(request, "Rezervasyonunuz alınmıştır. Rezervasyon bilgileriniz profil sayfanızda listelenmektedir. Gelişmeleri takip edebilirsiniz. Teşekkür ederiz.")
            return HttpResponseRedirect(url)
        messages.error(request, "Lütfen boş bırakılan yerleri doldurunuz...!")
    return HttpResponseRedirect(url)
