from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CreateAnswerForm, UpdateAnswerForm
from .models import Answer
from ..questions.models import Question
from ..accounts.models import User


# Answer mixin
class AnswerMixin(object):
    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.question_id.pk})


# create answer with login required
class CreateAnswer(AnswerMixin, CreateView, LoginRequiredMixin):
    form_class = CreateAnswerForm
    template_name = 'answers/create.html'
    success_url = 'questions:detail'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override form valid func
    def form_valid(self, form):
        # get id question or None
        question_id = self.kwargs.get('pk', None)
        if question_id is not None:
            # set foreign key for question and user
            form.instance.question_id = Question.objects.get(id=question_id)
            form.instance.user_id = User.objects.get(id=self.request.user.id)
            return super().form_valid(form)
        return self.form_invalid(form)


# update answer with login required
class UpdateAnswer(AnswerMixin, UpdateView, LoginRequiredMixin):
    form_class = UpdateAnswerForm
    model = Answer
    template_name = 'answers/update.html'
    success_url = 'questions:detail'
    # login required settings
    login_url = '/'
    redirect_field_name = None


# delete answer with login required
class DeleteAnswer(AnswerMixin, DeleteView, LoginRequiredMixin):
    template_name = 'answers/delete.html'
    model = Answer
    success_url = 'questions:detail'
    # login required settings
    login_url = '/'
    redirect_field_name = None





