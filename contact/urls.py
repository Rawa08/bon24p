from django.urls import path
from .views import get_contact_page, send_email


urlpatterns = [
    path('', get_contact_page, name='contact_page'),
    path('send', send_email, name='send_email'),
    
    
]