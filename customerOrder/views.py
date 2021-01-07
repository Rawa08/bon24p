from django.shortcuts import render, get_object_or_404, reverse, redirect, get_list_or_404
import os
from django.contrib import messages
from .forms import CustomerShippingForm
from .models import ProductList
from django.utils import timezone
from product.models import Product
from templated_email import send_templated_mail



# Create your views here.



admin_mail = os.getenv('admin_email')

def checkout(request):
    
    
    if request.method == "POST":
        order_form = CustomerShippingForm(request.POST)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = ProductList(
                        orderBy=order,
                        quantity=quantity,
                        products=product
                )
                
                
                
                order_line_item.save()
                
            myProducts = get_list_or_404(ProductList, orderBy=order)
                
            send_templated_mail(
        template_name='welcome',
        from_email=admin_mail,
        recipient_list=[order.email],
        context={'username':order.name,
'Products':myProducts,
'total':total
        },
        # Optional:
        # cc=['cc@example.com'],
        bcc=[admin_mail],
        headers={'My-Custom-Header':'Your order from Shex Ater'},
        # template_prefix="my_emails/",
        # template_suffix="email",
)           
            messages.error(request, "Thank you for your order, we contact you soon!")
            request.session['cart'] = {}
            
            return redirect(reverse('home'),{'messages':messages})
             
        else:
            order_form = CustomerShippingForm()
            messages.error(
                request, "Please fill the contactform")
               
    else:
        
        order_form = CustomerShippingForm()

    return render(request, "checkout.html", {'order_form': order_form})

