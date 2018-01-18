from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .forms import UserCreationForm, UserLoginForm

# Create your views here.


class CreateUser(CreateView):
    template_name = 'auth/create.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class LoginUser(FormView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm
    success_url = '/'



