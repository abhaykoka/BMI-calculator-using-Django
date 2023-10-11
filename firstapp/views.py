from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import OrderForm

def home(request):
    return render(request,'home.html',{'name':'Abhay'})
def bmi(request):
    val1=float(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val2/(val1*val1)
    return render(request,'result.html',{'result':res})

def dashboard(request):
    ord = Order.objects.all()
    customers=Customer.objects.all()
    return render(request, 'dashboard.html',{'customers':customers, 'ord':ord})
def products(request):    
    p=Product.objects.all()
   
    return render(request,'products.html')
  
'''def ourproducts(request):
    p=Product.objects.all()
    return render(request,'products.html',{'prod':p})  '''

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    customers=Customer.objects.all()
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customers':customers, 'cust':customer,'ord':orders,'ordcount':order_count}
    return render(request, 'customer.html', context)
def createOrder(request):
    form = OrderForm()

    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}

    return render(request,'order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'order_form.html',context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)

    if request.method=="POST":
        order.delete()
        return redirect("/")

    context={'item':order}

    return render(request,'delete.html',context)
'''from django.shortcuts import render

from .models import *

def home(request):
    return render(request,'home.html',{'name':'Siddartha'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})

def dashboard(request):
    customers=Customer.objects.all()
    return render(request,'dashboard.html',{'customers':customers})

def products(request):
    return render(request,'products.html')

def hi(request):
    return render(request,'hi.html')

# def customer(request,pk_test):
#     customers=Customer.objects.get(id=pk_test)
#     customers=Customer.objects.all()'''