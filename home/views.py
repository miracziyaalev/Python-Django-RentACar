from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment


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

def product_detail(request,id,slug):


   category = Category.objects.all()
   product = Product.objects.get(pk=id)
   comments = Comment.objects.filter(product_id=id, status='True')
   images = Images.objects.filter(product_id=id)
   context = {'category': category,
              'comments': comments,
              'product': product,
              'images': images,
              }
   return render(request, 'product_detail.html', context)

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

def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)

            context = {
                'products' : products,
                'category' : category,
            }
            return render(request, 'products_search.html', context)

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    # Redirect to a success page.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
            ...
        else:
            messages.error(request, "Hata! Kullanıcı adı veya şifre hatalı.")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)
