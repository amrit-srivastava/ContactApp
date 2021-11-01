from django.shortcuts import reverse, redirect
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
            return Contacts.objects.filter(
                user=self.request.user, firstName__icontains=searched
            )
        return Contacts.objects.filter(user=self.request.user)


class ContactCreateView(CreateView):
    template_name = "contacts/add.html"
    form_class = AddContactForm
    success_url = reverse_lazy("contacts:list-view")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
        return redirect(reverse("contacts:list-view"))


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
