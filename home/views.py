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
    dayproducts=Product.objects.all()[:6]
    lastproducts = Product.objects.all().order_by('-id')[:6]
    randomproducts = Product.objects.all().order_by('?')[:6]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get()
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page': hakkimizda}
    return render(request, 'hakkimizda.html', context)

def category_products(request,id,slug):
    products = Product.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    context = { 'category': category, 'products': products, 'categorydata': categorydata}
    return render(request, 'products.html', context)

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
