import django.urls

from . import views

urlpatterns = [
    # ex: /polls/
    django.urls.path('', views.index, name='index'),
    django.urls.path('update/', views.user_update, name='user_update'),
    django.urls.path('password/', views.change_password, name='change_password'),
    django.urls.path('comments/', views.comments, name='comments'),
    django.urls.path('deletecomment/<int:id>', views.deletecomment, name='deletecomment')

    #django.urls.path('addcomment/<int:id>', views.addcomment, name='addcomment')



    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]