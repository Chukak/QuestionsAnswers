from django.shortcuts import redirect
from django.core.urlresolvers import resolve
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


# override dispatch method for redirect
class AccountDispatchMixin(object):
    def dispatch(self, request, *args, **kwargs):
        # get user
        user = User.objects.get(id=kwargs['pk'])
        # user == request.user
        if user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        else:
            # Example:
            # this happened, if url - /accounts/9/ change to /accounts/10/ but user.id == 9
            # redirect to correct url for this user
            # this method only fo accounts
            url = resolve(request.path).url_name
            return redirect('accounts:' + str(url), pk=request.user.id)


# detail view account with login required ans mixin
class AccountDetail(AccountDispatchMixin, DetailView, AccountsMixin, LoginRequiredMixin):
    template_name = 'accounts/detail.html'
    model = User
    # setting for login required
    redirect_field_name = None
    login_url = '/'

    # get object in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        # select object from table where user_id=self.object.id order by date_created desc limit 6
        context['questions'] = list(Question.objects.filter(user_id=self.object.id).order_by('-date_created')[:6])
        context['answers'] = list(Answer.objects.filter(user_id=self.object.id).order_by('-date_created')[:6])
        return context


# update view account with login required and mixin
class AccountUpdate(AccountDispatchMixin, UpdateView, AccountsMixin, LoginRequiredMixin):
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
class AccountDelete(AccountDispatchMixin, DeleteView, AccountsMixin, LoginRequiredMixin):
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
class ListUserAnswers(AccountDispatchMixin, ListView, LoginRequiredMixin):
    template_name = 'accounts/user_answers.html'
    model = Answer
    paginate_by = 5
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # get queryset
    def get_queryset(self):
        return Answer.objects.filter(user_id=self.kwargs['pk'])


# list user questions
class ListUserQuestions(AccountDispatchMixin, ListView, LoginRequiredMixin):
    template_name = 'accounts/user_questions.html'
    model = Question
    paginate_by = 5
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # get queryset
    def get_queryset(self):
        return Question.objects.filter(user_id=self.kwargs['pk'])



