from django.shortcuts import get_object_or_404
from product.models import Product, Brand
from django.http import JsonResponse



def cart_content(request):
    """
    retriving cart item from session, make it avilable to render on other pages
    """
    quantityRange = range(1, 99)
    brand = Brand.objects.all().order_by('name')
    cart = request.session.get('cart', {})

    


    cart_item = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, id=id)
        total += quantity * product.price
        product_count += quantity
        cart_item.append({'id': id, 'quantity': quantity, 'product': product})
    

    return {'cart_item': cart_item, 'total': total, 'product_count': product_count , 'brand':brand, 'range':quantityRange}



    