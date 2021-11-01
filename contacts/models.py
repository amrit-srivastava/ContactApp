from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("contacts:detail-view", kwargs={"pk": self.id})

    def get_update_url(self):
        return reverse("contacts:update-view", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("contacts:delete-view", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.firstName}"
