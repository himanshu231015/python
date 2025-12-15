from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, ImageUploader, Product, Cart, CartItem
from django.contrib.auth import authenticate, login
from .forms import ProductForm

# Create your views here.
def index(request):
    name = request.session.get('name')
    return render(request, 'index.html', {'name': name})

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
    name = request.session.get('name')
    if name:
        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'login.html')

def login(request):
    request.session.flush()
    if request.method == 'POST':
        unm1 = request.POST.get('unm')
        pw1 = request.POST.get('pw')
        try:
            # Corrected lookup to check both username and password
            data = Customer.objects.get(unm=unm1, pw=pw1)
            request.session['name'] = unm1
            return redirect('/')
        except Customer.DoesNotExist:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def why(request):
    name = request.session.get('name')
    return render(request, 'why.html', {'name': name})

def testimonial(request):
    name = request.session.get('name')
    return render(request, 'testimonial.html', {'name': name})

def shop(request):
    name = request.session.get('name')
    products = Product.objects.all()
    return render(request, 'shop.html', {'name': name, 'products': products})

def upload_image(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        image_uploader_obj = ImageUploader()
        image_uploader_obj.photo = request.FILES['image']
        image_uploader_obj.save()
    all_image = ImageUploader.objects.all()
    return render(request=request, template_name="ImageUpload.html", context={'img': all_image})

def delete_image(request, id):
    if request.method == 'POST':
        image = get_object_or_404(ImageUploader, id=id)
        image.delete()
        return redirect('upload_image')
    return redirect('upload_image')

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        
        # Get or create session key
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key

        # Get or create cart
        cart, created = Cart.objects.get_or_create(session_id=session_id)
        
        # Get or create cart item
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('cart')
    return redirect('shop')

def remove_from_cart(request, cart_item_id):
    if request.method == 'POST':
        # Get session id to ensure user owns the cart
        session_id = request.session.session_key
        if session_id:
            cart = get_object_or_404(Cart, session_id=session_id)
            item = get_object_or_404(CartItem, id=cart_item_id, cart=cart)
            item.delete()
    return redirect('cart')

def cart(request):
    name = request.session.get('name')
    session_id = request.session.session_key
    cart_items = []
    total_price = 0
    
    if session_id:
        try:
            cart = Cart.objects.get(session_id=session_id)
            cart_items = cart.items.all()
            total_price = sum(item.get_total_price() for item in cart_items)
        except Cart.DoesNotExist:
            pass
            
    return render(request, 'cart.html', {'name': name, 'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    session_id = request.session.session_key
    if session_id:
        try:
            cart = Cart.objects.get(session_id=session_id)
            cart.items.all().delete() # Clear items
            # In a real app, you would process payment and create an Order here
        except Cart.DoesNotExist:
            pass
    return redirect('shop')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})