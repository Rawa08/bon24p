from django.shortcuts import render,redirect, reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os


emaila_account = os.getenv('defaul_email')
# Create your views here.
def get_contact_page(request):
#render contact page
    return render(request, 'contact.html')
   
    

#Send email thrue smtp 
def send_email(request):
    subject = request.POST.get('name')
    message = request.POST.get('text')
    from_email = request.POST.get('from_email')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [emaila_account])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request,"Thank you for your request, we contact you soon!")    
        return redirect(reverse('home'),{'messages':messages})
    else:
        messages.error(request, "Please fill out all fields")
      
        return redirect(reverse('contact_page'))
