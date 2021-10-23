from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from contacts.forms import AddContactForm
from .models import Contacts


class ContactListView(ListView):
    paginate_by = 5
    model = Contacts
    template_name = "contacts/listview.html"
    ordering = ["firstName"]
    queryset = Contacts.objects.all()


def contactHomeView(request):
    return render(request, "contacts/home.html", {})


def contactCreateView(request):
    form = AddContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddContactForm()

    context = {"form": form}
    return render(request, "contacts/add.html", context)


def contactUpdateView(request, id):
    obj = Contacts.objects.get(id=id)
    form = AddContactForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = AddContactForm()

    context = {"form": form}
    return render(request, "contacts/update.html", context)


def ContactDetailView(request, id):
    obj = Contacts.objects.get(id=id)
    context = {"obj": obj}

    return render(request, "contacts/detail.html", context)


def ContactDeleteView(request, id):
    obj = get_object_or_404(Contacts, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("http://127.0.0.1:8000/contacts/")

    context = {"obj": obj}

    return render(request, "contacts/delete.html", context)


def contactSearchView(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        contact = Contacts.objects.filter(firstName__contains=searched)
        return render(
            request, "contacts/search.html", {"searched": searched, "contact": contact}
        )

    else:
        return render(request, "contacts/search.html", {})
