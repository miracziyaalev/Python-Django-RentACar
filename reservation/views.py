from django.http import HttpResponse

from reservation.models import Reservation, ReservationFormu


def index(request):
    return HttpResponse('Reservation App')

from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import CommentForm, Comment


@login_required(login_url='/login')

def addreservation(request, id):

    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReservationFormu(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Reservation()
            data.user_id = current_user.id
            data.product_id = id
            data.rezdate = form.cleaned_data['rezdate']
            data.reztime = form.cleaned_data['reztime']
            data.returndate = form.cleaned_data['returndate']
            data.returntime = form.cleaned_data['returntime']
            data.rezplace = form.cleaned_data['rezplace']
            data.returnplace = form.cleaned_data['returnplace']
            data.days = form.cleaned_data['days']



            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Rezervazyon Talebiniz Basariyla Gonderilmistir.")
            return HttpResponseRedirect(url)


    return HttpResponseRedirect(url)
