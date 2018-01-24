from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.utils.translation import gettext_lazy as _
from ..answers.models import Answer
from ..questions.models import Question
from .models import User
from .forms import UserUpdateForm


# mixin class for get object from pk
class AccountsMixin(object):
    def get_object(self, queryset=None):
        # get pk from kwargs and return user object
        return self.model.object.get(id=self.kwargs['pk'])


# detail view account with login required ans mixin
class AccountDetail(DetailView, AccountsMixin, LoginRequiredMixin):
    template_name = 'accounts/detail.html'
    model = User
    # setting for login required
    redirect_field_name = None
    login_url = '/'

    # get object in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context


# update view account with login required and mixin
class AccountUpdate(UpdateView, AccountsMixin, LoginRequiredMixin):
    template_name = 'accounts/update.html'
    form_class = UserUpdateForm
    model = User
    success_url = 'accounts:detail'
    # settings for login required
    redirect_field_name = None
    login_url = '/'

    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.pk})


# Delete view with login required ans mixin
class AccountDelete(DeleteView, AccountsMixin, LoginRequiredMixin):
    model = User
    template_name = 'accounts/delete.html'
    success_url = '/'
    # settings for login required
    login_url = '/'
    redirect_field_name = None
    # custom field

    # override post method
    def post(self, request, *args, **kwargs):
        # set self.object
        self.object = self.get_object()
        # check password for user and if true return delete method
        if self.object.check_password(request.POST.get('password_confirm')):
            return self.delete(request, *args, **kwargs)
        else:
            # set error to context and response template
            context = super().get_context_data(**kwargs)
            context['error'] = _('Invalid password')
            return self.render_to_response(context=context)

    # override delete method for delete file image from path
    def delete(self, request, *args, **kwargs):
        self.object.avatar.delete(save=True)
        return super().delete(request, *args, **kwargs)


# list user answers
class ListUserAnswers(ListView, LoginRequiredMixin):
    template_name = 'accounts/user_answers.html'
    model = Answer
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # get queryset
    def get_queryset(self):
        return Answer.objects.filter(user_id=self.kwargs['pk'])


# list user questions
class ListUserQuestions(ListView, LoginRequiredMixin):
    template_name = 'accounts/user_questions.html'
    model = Question
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # get queryset
    def get_queryset(self):
        return Question.objects.filter(user_id=self.kwargs['pk'])



