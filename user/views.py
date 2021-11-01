from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "user/register.html"
    success_url = reverse_lazy("user:login")
    form_class = UserRegisterForm
    success_message = (
        "Your profile was created successfully, Log in now to enter Contact App"
    )
