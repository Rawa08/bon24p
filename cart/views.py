from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.http import JsonResponse







# Create your views here.


def my_cart(request):
    cart_template = 'cart.html'
    cart = request.session.get('cart', {})
    if not cart.items():
        messages.error(request, "Your cart is empty")
        return redirect(reverse('home'),{'messages':messages})
    else:
        return render(request, cart_template ,{'range':range(1,100)})

    
def add_product(request):
    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('post_id') 
        quantity = int(request.POST.get('quantity'))
        
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] = int(cart[id]) + quantity
        else:
            cart[id] = cart.get(id, quantity)
        request.session['cart'] = cart
        
        return HttpResponse('')

    else:
        return redirect(reverse('home'))     
            
     
    
        



def adjust(request, id):

    # Adjust the quantity of the specified product to the specified amount

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('my_cart'))


def delete_from_cart(request, id):

    # Remove item from cart

    quantity = int(0)
    cart = request.session.get('cart', {})
    cart[id] = quantity
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('my_cart'))

"""
def item_quantity(request):
    cart = request.session.get('cart', {})
    
    for id, quantity in cart.items():
        pCount +=quantity
    print("item_quantity requested")
    return JsonResponse({'pCount':pCount})
"""    