from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateAnswerForm, UpdateAnswerForm
from .models import Answer
from ..questions.models import Question
from ..accounts.models import User


# Answer mixin
class AnswerMixin(object):
    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'question': self.object.question_id.pk})


# create answer with login required
class CreateAnswer(AnswerMixin, CreateView, LoginRequiredMixin):
    form_class = CreateAnswerForm
    template_name = 'answers/create.html'
    success_url = 'questions:detail'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override get method
    def get(self, request, *args, **kwargs):
        # try get answer objects
        try:
            # if get object, set kwargs object id and redirect update answer view
            answer = Answer.objects.get(question_id=kwargs['question'], user_id=self.request.user.id)
            kwargs['answer'] = answer.id
            return redirect('answers:update', **kwargs)
        # else return get method
        except ObjectDoesNotExist:
            return super().get(request, *args, **kwargs)

    # override form valid func
    def form_valid(self, form):
        # get id question or None
        question_id = self.kwargs.get('question', None)
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
    # get args from url
    pk_url_kwarg = 'answer'
    # login required settings
    login_url = '/'
    redirect_field_name = None


# delete answer with login required
class DeleteAnswer(AnswerMixin, DeleteView, LoginRequiredMixin):
    template_name = 'answers/delete.html'
    model = Answer
    success_url = 'questions:detail'
    # get args from url
    pk_url_kwarg = 'answer'
    # login required settings
    login_url = '/'
    redirect_field_name = None


# ///////////////////////////////////////////////////////////







