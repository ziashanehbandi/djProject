from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import random


# Create your views here.

def first_page(request):
    return HttpResponse('this is first page')

def second_page(request):
    return render(request,'djangoProject/test.html')

def password(request):
    length=int(request.GET.get('length'))
    charlist=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charlist.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        charlist.extend('0123456789')
    if request.GET.get('specificchars'):
        charlist.extend('!@#$%^&*()_+')
    thepassword=''
    for num in range(length):
        thepassword += random.choice(charlist)

    return render(request,'djangoProject/test1.html',{'passwords': thepassword})

def about_page(request):
    return JsonResponse({ 'author':'ziashanehbandi',
              'age':20,
              'job':'bachend develepor',
    })

