from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



from reservation.models import ReservationForm, Reservation


def index(request):
    return HttpResponse("Reserve Page")



@login_required(login_url="/login")
def sendreserve(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = Reservation()  # create relation with model
            data.reztime = form.cleaned_data['reztime']
            data.returntime = form.cleaned_data['returntime']
            data.returndate = form.cleaned_data['returndate']
            data.rezdate = form.cleaned_data['rezdate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Rezervasyonunuz Alınmıştır. Teşekkür ederiz.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
