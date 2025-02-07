from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Testimonial
from django.http import JsonResponse

def home(request):
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()
    cart_items = request.session.get('cart', [])
    cart_count = sum([item['quantity'] for item in cart_items])
    return render(request, 'shop/home.html', {'products': products, 'cart_count': cart_count, 'testimonials': testimonials})

def cart(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = []
    total = 0
    for item in cart_items:
        product = Product.objects.get(id=item['product_id'])
        products_in_cart.append({'product': product, 'quantity': item['quantity']})
        total += product.price * item['quantity']
    return render(request, 'shop/cart.html', {'cart_items': products_in_cart, 'total': total})

def checkout(request):
    return render(request, 'shop/checkout.html')


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart = request.session.get('cart', [])
        
        existing_item = next((item for item in cart if item['product_id'] == product_id), None)
        if existing_item:
            existing_item['quantity'] += 1
        else:
            cart.append({'product_id': product_id, 'quantity': 1})
        
        request.session['cart'] = cart
        
        cart_count = sum([item['quantity'] for item in cart])
        return JsonResponse({'success': True, 'cart_count': cart_count})
    return JsonResponse({'success': False})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    
    existing_item = next((item for item in cart if item['product_id'] == product_id), None)
    
    if existing_item:
        if existing_item['quantity'] > 1:
            existing_item['quantity'] -= 1
        else:
            cart = [item for item in cart if item['product_id'] != product_id]
    
    request.session['cart'] = cart
    
    return redirect('cart')  

