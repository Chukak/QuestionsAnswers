from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateQuestionForm, UpdateQuestionForm
from ..accounts.models import User
from .models import Question


# create view with login required
class CreateQuestion(CreateView, LoginRequiredMixin):
    template_name = 'questions/create.html'
    form_class = CreateQuestionForm
    success_url = '/'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override form valid for set user object to user_id field of questions
    def form_valid(self, form):
        # get user object
        user = User.objects.get(id=self.request.user.id)
        # set this in form
        form.instance.user_id = user
        return super().form_valid(form)


# update view with login required
class UpdateQuestion(UpdateView, LoginRequiredMixin):
    template_name = 'questions/update.html'
    form_class = UpdateQuestionForm
    model = Question
    success_url = 'questions:update'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.pk})


# delete view with login required
class DeleteQuestion(DeleteView, LoginRequiredMixin):
    template_name = 'questions/delete.html'
    model = Question
    success_url = '/'
    # login required settings
    login_url = '/'
    redirect_field_name = None



