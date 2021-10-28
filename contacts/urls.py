from django.urls import path
from .views import (
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
)

app_name = "contacts"

urlpatterns = [
    path("contacts/<int:pk>", ContactDetailView.as_view(), name="detail-view"),
    path("add/", ContactCreateView.as_view(), name="add-view"),
    path("", ContactListView.as_view(), name="list-view"),
    path("contacts/<int:pk>/update", ContactUpdateView.as_view(), name="update-view"),
    path("contacts/<int:pk>/delete", ContactDeleteView.as_view(), name="delete-view"),
]
