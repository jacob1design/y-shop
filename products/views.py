from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(uuid=id)
    return render(request, 'products/product-detail.html', {'product' : product})

@login_required
def buy(request, product_id):
    product = Product.objects.get(uuid=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['delivery_address']
            phone_number = form.cleaned_data['phone_number']
            Order.objects.create(user=request.user, 
            delivery_address=address, phone_number=phone_number, total = product.price, product=product)
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'products/buy.html', {'form' : form, 'product' : product})


@login_required
def user_orders(request):
    orders = request.user.orders
    return render(request, 'products/orders.html', {'orders' : orders})