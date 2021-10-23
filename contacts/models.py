from django.db import models
from django.urls import reverse


class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contactNumber = models.IntegerField(default=None)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("detail-view", kwargs={"id": self.id})

    def get_absolute_url1(self):
        return reverse("update-view", kwargs={"id": self.id})

    def get_absolute_url2(self):
        return reverse("delete-view", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.contactNumber} {self.email} {self.address}"
