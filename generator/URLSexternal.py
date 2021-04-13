from django.urls import path
from generator.views import *

urlpatterns = [

    path('',first_page,name='first'),
    path('sec',second_page,name='second'),
    path('password/',password),
    path('about',about_page, name='about')

]