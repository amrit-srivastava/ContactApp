from django.db import models
from django.urls import reverse


class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contactNumber = models.IntegerField(default=None)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("contacts:detail-view", kwargs={"pk": self.id})

    def get_update_url(self):
        return reverse("contacts:update-view", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("contacts:delete-view", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.firstName}"
