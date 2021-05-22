import django.urls

from . import views

urlpatterns = [
    # ex: /polls/
    django.urls.path('', views.index, name='index'),
    #django.urls.path('addcomment/<int:id>', views.addcomment, name='addcomment')



    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]