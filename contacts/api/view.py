# from django.db.models.query import QuerySet
from rest_framework import generics
from contacts.models import Contacts
from .serializers import ContactsSerializers
from django.db.models import Q


class ContactsRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = ContactsSerializers

    def get_queryset(self):
        return Contacts.objects.all()


class ContactsLCView(generics.ListCreateAPIView):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()

    def get_queryset(self):
        qs = Contacts.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(firstName__icontains=query) | Q(address__icontains=query)
            ).distinct()
        return qs
