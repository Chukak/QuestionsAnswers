from django.shortcuts import redirect, Http404
from django.core.urlresolvers import resolve
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
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


# Answer context mixin
class AnswerContextMixin(object):
    # get question object in template for create and update view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(id=self.kwargs['question'], user_id=self.request.user.id)
        context['question'] = question
        return context


# override dispatch method for redirect
class AnswerDispatchMixin(object):
    def dispatch(self, request, *args, **kwargs):
        # get user
        try:
            # get answer
            answer_ = Answer.objects.get(id=kwargs['answer'])
            # user == request.user
            if answer_.user_id.id == request.user.id:
                return super().dispatch(request, *args, **kwargs)
            else:
                # Example:
                # this happened, if url - /answers/9/ change to /answers/10/ but user_id != request.user.id
                # raise 404
                # this method only fo questions
                raise Http404
        # if not answer
        except ObjectDoesNotExist:
            raise Http404


# create answer with login required
class CreateAnswer(AnswerMixin, AnswerContextMixin, CreateView, LoginRequiredMixin):
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
class UpdateAnswer(AnswerDispatchMixin, AnswerMixin, AnswerContextMixin, UpdateView, LoginRequiredMixin):
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
class DeleteAnswer(AnswerDispatchMixin, AnswerMixin, DeleteView, LoginRequiredMixin):
    template_name = 'answers/delete.html'
    model = Answer
    success_url = 'questions:detail'
    # get args from url
    pk_url_kwarg = 'answer'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override post method
    def post(self, request, *args, **kwargs):
        # set self.object
        self.object = self.get_object()
        # get user object
        user = User.objects.get(id=request.user.pk)
        # check password for user and if true return delete method
        if user.check_password(request.POST.get('password_confirm')):
            return self.delete(request, *args, **kwargs)
        else:
            # set error to context and response template
            context = super().get_context_data(**kwargs)
            context['error'] = _('Invalid password')
            return self.render_to_response(context=context)


# ///////////////////////////////////////////////////////////







