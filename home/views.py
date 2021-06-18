from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ
from product.models import Product, Category, Images, Comment


def index(request):
    setting = Setting.objects.get()
    sliderdata = Product.objects.all().order_by('?')[:6]
    bannerdata1 = Product.objects.all().filter(category_id=10)[:1]
    bannercon1 = Product.objects.all().filter()
    suvs = Product.objects.all().filter(category__parent_id=5)[:10]
    sedan = Product.objects.all().filter(category__parent_id=12)[:10]
    hatchback = Product.objects.all().filter(category__parent_id=8)[:10]
    bannerdata2 = Product.objects.all().order_by('-id')[:1]
    category = Category.objects.all()
    dayproducts=Product.objects.all()[:6]

    lastproducts = Product.objects.all().order_by('-id')[:6]
    randomproducts = Product.objects.all().order_by('?')[:6]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'bannerdata1': bannerdata1,
               'bannerdata2': bannerdata2,
               'dayproducts': dayproducts,
               'bannercon1': bannercon1,
               'suvs': suvs,
               'sedan': sedan,
               'hatchback': hatchback,
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

        else:
            messages.error(request, "Hata! Kullanıcı adı veya şifre hatalı..!")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, "Hoş geldiniz. Sitemize başarıyla üye oldunuz..!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Hata! Belirtilen kriterlere uyulmadi!")
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    category = Category.objects.all()
    context = {
            'category': category,
            'form': form,
        }
    return render(request, 'signup.html', context)

def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {
        'category': category,
        'faq' : faq,
    }
    return render(request, 'faq.html', context)


