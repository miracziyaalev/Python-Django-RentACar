from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get()
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page': 'home', 'sliderdata': sliderdata}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get()
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.")
            return HttpResponseRedirect ('/iletisim')
        
    setting = Setting.objects.get()
    category = Category.objects.all()
    form = ContactFormu()
    context={'setting':setting, 'category': category, 'form':form}
    return render(request, 'iletisim.html', context)
