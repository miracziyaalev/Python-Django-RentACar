import django.urls

from . import views

urlpatterns = [
    # ex: /polls/
    django.urls.path('', views.index, name='index'),
    django.urls.path('sendreserve/<int:id>', views.sendreserve, name='sendreserve')




    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]