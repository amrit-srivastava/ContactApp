from django.urls import path
from .views import (
    ContactListView,
    ContactDetailView,
    contactCreateView,
    contactUpdateView,
    ContactDeleteView,
    contactSearchView,
    contactHomeView,
)


urlpatterns = [
    path("contacts/", ContactListView.as_view(), name="list-view"),
    path("contacts/<int:id>", ContactDetailView, name="detail-view"),
    path("add/", contactCreateView, name="add-view"),
    path("", contactHomeView, name="home-view"),
    path("search/", contactSearchView, name="search-view"),
    path("contacts/<int:id>/update", contactUpdateView, name="update-view"),
    path("contacts/<int:id>/delete", ContactDeleteView, name="delete-view"),
]
