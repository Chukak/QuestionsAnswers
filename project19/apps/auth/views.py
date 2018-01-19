from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from .forms import UserCreationForm, UserLoginForm
from .utils import check_user_auth

# Create your views here.


class CreateUser(CreateView):
    template_name = 'auth/create.html'
    form_class = UserCreationForm
    success_url = '/'

    # add decorator for this view. This view not authenticated users only.
    # check utils module
    @method_decorator(user_passes_test(check_user_auth, login_url='/', redirect_field_name=None))
    # dispatch override with decorator
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # get and del 3 required args from dict
        username = form.cleaned_data.pop('username', None)
        password = form.cleaned_data.pop('password', None)
        email = form.cleaned_data.pop('email', None)
        if email and password and username:
            user = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                        **form.cleaned_data)  # get other args
            if user:
                # set saved user object
                self.object = user
                # login after registration
                auth = authenticate(username=username, password=password)
                if auth is not None:
                    login(self.request, auth)
                    return redirect(self.get_success_url())
        return super().form_invalid(form)


class LoginUser(FormView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm
    success_url = '/'

    # add decorator for this view. This view not authenticated users only.
    # check utils module
    @method_decorator(user_passes_test(check_user_auth, login_url='/', redirect_field_name=None))
    # dispatch override with decorator
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_auth = authenticate(self.request, username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password'])
        if user_auth is not None:
            login(self.request, user_auth)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


# this view only authenticated user
@login_required(redirect_field_name=None, login_url='/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


