from django import forms
from .models import Customer, ProductList


    
class CustomerShippingForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class':'form-control',
            'placeholder':'Name',
            'id':'name'

        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class':'form-control',
            'placeholder':'Phone number / Viber / Whatsup / etc..',
            'id':'phone'

        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class':'form-control',
            'id':'exampleInputEmail1',
            'aria-describedby':"emailHelp",
            'placeholder':'Email'

        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class':'form-control',
            'placeholder':'City',
            'id':'city'

        }
    ))
    

    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'city')