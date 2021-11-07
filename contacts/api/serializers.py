from rest_framework import serializers
from contacts.models import Contacts


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            "pk",
            "firstName",
            "lastName",
            "contactNumber",
            "email",
            "address",
            "user",
        ]
