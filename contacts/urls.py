from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
)

app_name = "contacts"

urlpatterns = [
    path(
        "contacts/<int:pk>",
        login_required(ContactDetailView.as_view()),
        name="detail-view",
    ),
    path("add/", login_required(ContactCreateView.as_view()), name="add-view"),
    path("contacts/", login_required(ContactListView.as_view()), name="list-view"),
    path(
        "contacts/<int:pk>/update",
        login_required(ContactUpdateView.as_view()),
        name="update-view",
    ),
    path(
        "contacts/<int:pk>/delete",
        login_required(ContactDeleteView.as_view()),
        name="delete-view",
    ),
]
