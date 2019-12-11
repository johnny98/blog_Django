from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('', views.index, name='index'),
    path('formpage/',views.form_page,name='form_npage'),
]
