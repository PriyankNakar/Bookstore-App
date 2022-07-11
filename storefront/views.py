
from typing import Counter
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
import json
# Create your views here.


def index(request):
    if "items" not in request.session:
        request.session["items"]=[]
    
    products=models.Product.objects.all()
    if request.user.username:
        return render(request,'storefront/index.html',{"products":products,"cartlen":lenofcart(request)})
    return redirect('Login')

def addbook(request):
    if request.user.username:
        return render(request,'storefront/addbook.html',{"cartlen":lenofcart(request)})
    return redirect('Login')
def bookadd(request):
    if request.method=='POST':
        if request.user.is_superuser:
            instance=models.Product()
            instance.book_title=request.POST['title']
            instance.book_desc=request.POST['desc']
            instance.book_price=request.POST['price']
            instance.book_Image=request.FILES['image']
            
            instance.save()
            return redirect ('index')
        else:
            return redirect('index')
    else:
        return redirect('index')

def searchbook(request):
    if request.method=='POST':
        if request.user.username:
            search_items=models.Product.objects.filter(book_title__icontains=request.POST['bookname'])
           
            return render(request,'storefront/index.html',{"searchItems":search_items,"cartlen":lenofcart(request)})
        else:
           return redirect('Login')
    else:
        return redirect('Login')

def addtocart(request):
    if request.method=='POST':
        if request.user.username:
            cart=json.loads(request.body)
        
            request.session["items"]+=[cart]
            return HttpResponse(status=200)
    return HttpResponse(status=200)

def lenofcart(request):
    quantity=Counter(request.session["items"])
    quantity=dict(quantity)
    return len(quantity)
def cart(request):
    if request.user.username:
        quantity=Counter(request.session["items"])
        quantity=dict(quantity)
    
        cart_item=models.Product.objects.filter(id__in=request.session["items"])
    
        return render(request,'storefront/cart.html',{'cart_item':cart_item,'quant':quantity,"cartlen":lenofcart(request)})
    else:
        return redirect('index')
def deleteelement(request):
    if request.method=='POST':
        if request.user.username:
            cart=json.loads(request.body)
            while cart in request.session['items']:request.session['items'].remove(cart)
            request.session.modified = True
            return HttpResponse(status=200)
    return redirect('index')