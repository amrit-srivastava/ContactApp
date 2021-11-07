from django.urls import path
from .view import ContactsRudView, ContactsLCView


app_name = "contacts"
urlpatterns = [
    path("<int:pk>", ContactsRudView.as_view(), name="post-rud"),
    path("", ContactsLCView.as_view(), name="post-lc"),
]
