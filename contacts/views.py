from django.shortcuts import render, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from contacts.forms import AddContactForm
from .models import Contacts
from django.urls import reverse_lazy


class ContactListView(ListView):
    paginate_by = 5
    model = Contacts
    template_name = "contacts/listview.html"
    ordering = ["firstName"]

    def get_queryset(self):
        searched = self.request.GET.get("searched")
        if searched:
            return Contacts.objects.filter(firstName__icontains=searched)
        return Contacts.objects.all()


class ContactCreateView(CreateView):
    template_name = "contacts/add.html"
    form_class = AddContactForm
    success_url = reverse_lazy("contacts:list-view")


class ContactUpdateView(UpdateView):
    form_class = AddContactForm
    queryset = Contacts.objects.all()
    template_name = "contacts/update.html"

    def get_success_url(self):
        pk = self.kwargs.get("pk")

        return reverse("contacts:detail-view", kwargs={"pk": pk})


class ContactDetailView(DetailView):
    model = Contacts
    template_name = "contacts/detail.html"
    context_object_name = "obj"


class ContactDeleteView(DeleteView):
    model = Contacts
    context_object_name = "obj"
    template_name = "contacts/delete.html"
    success_url = reverse_lazy("contacts:list-view")
