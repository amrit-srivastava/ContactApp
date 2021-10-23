from django import forms
from .models import Contacts


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["firstName", "lastName", "contactNumber", "email", "address"]
