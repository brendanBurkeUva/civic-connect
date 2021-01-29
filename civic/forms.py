from django import forms
from .models import EmailTemp, Address

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailTemp
        fields = ['category', 'letter']
        labels = {'category': "Category: ", 'letter': "Email Template: "}

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']
        labels = {'address': "Address:"}
