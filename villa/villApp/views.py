from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer
from django.contrib.auth import aauthenticate,login
from django.shortcuts import redirect, get_object_or_404

from .models import ImageUploader


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



def upload_image(request):
    if request.method =='POST' and len(request.FILES) !=0:
        image_uploader_obj=ImageUploader()
        image_uploader_obj.photo =request.FILES['image']
        image_uploader_obj.save()
    all_image=ImageUploader.objects.all()
    return render(request=request, template_name="imageUpload.html",context={'img':all_image})


def delete_image(request,image_id):
    if request.method =='POST':
        obj = ImageUploader.objects.get(pk=image_id)
        obj.delete()
        return HttpResponseRedirect(redirect_to='ImageUpload.html')
    
def delete_image(request, id):

    if request.method == 'POST':
        
        image = get_object_or_404(ImageUploader, id=id)

        image.delete()
        return redirect('upload_image')

    return redirect('upload_image')