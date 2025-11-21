from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth import aauthenticate,login

# Create your views here.
def index(request):
    name=request.session.get('name')
    if name:
        context={'name':name}
        return render(request, 'index.html',{'name':name})
    else:
        return render(request, 'login.html')
def regis(request):
    if request.method == "POST":
        cname = request.POST['cnm']
        cadd = request.POST['cadd']
        email = request.POST['email']
        phone = request.POST['phone']
        unm = request.POST['unm']
        pw = request.POST['pw']

        cust = Customer(cname=cname, cadd=cadd, email=email, phone=phone, unm=unm, pw=pw)
        cust.save()

        return redirect('login')

    return render(request, 'regis.html')

        

def contact(request):
    return render(request, 'contact.html')
def userdtl(request):
    name=request.session.get('name')
    if name:
        context={'name':name}
        return render(request, 'index.html',{'name':name})
    else:
        return render(request, 'login.html')

def login(request):
    request.session.flush()
    if request.method == 'POST':
        unm1=request.POST.get('unm')
        pw1=request.POST.get('pw')
        try:
            data=Customer.objects.get(pw=pw1)
            request.session['name']=unm1
            return redirect('/')
        except:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def why(request):
    name=request.session.get('name')
    if name:
        context={'name':name}
        return render(request, 'index.html',{'name':name})
    else:
        return render(request, 'login.html')
def testimonial(request):
    name=request.session.get('name')
    if name:
        context={'name':name}
        return render(request, 'index.html',{'name':name})
    else:
        return render(request, 'login.html')
def shop(request):
    name=request.session.get('name')
    if name:
        context={'name':name}
        return render(request, 'index.html',{'name':name})
    else:
        return render(request, 'login.html')

