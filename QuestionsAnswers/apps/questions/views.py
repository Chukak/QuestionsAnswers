from django.shortcuts import redirect, Http404
from django.core.urlresolvers import resolve
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from .forms import CreateQuestionForm, UpdateQuestionForm
from ..accounts.models import User
from ..answers.models import Answer
from .models import Question


# mixin for dispatch
# override dispatch method for redirect
class QuestionDispatchMixin(object):
    def dispatch(self, request, *args, **kwargs):
        # try get question
        try:
            quest = Question.objects.get(id=kwargs['question'])
            # user == request.user
            if quest.user_id.id == request.user.id:
                return super().dispatch(request, *args, **kwargs)
            else:
                # Example:
                # this happened, if url - /questions/9/ change to /questions/10/ but user_id != request.user.id
                # raise 404
                # this method only fo questions
                raise Http404
        # if not question
        except ObjectDoesNotExist:
            raise Http404


# create view with login required
class CreateQuestion(CreateView, LoginRequiredMixin):
    template_name = 'questions/create.html'
    form_class = CreateQuestionForm
    success_url = 'questions:detail'
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

    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'question': self.object.pk})


# update view with login required
class UpdateQuestion(QuestionDispatchMixin, UpdateView, LoginRequiredMixin):
    template_name = 'questions/update.html'
    form_class = UpdateQuestionForm
    model = Question
    success_url = 'questions:update'
    # get args from url
    pk_url_kwarg = 'question'
    # login required settings
    login_url = '/'
    redirect_field_name = None

    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'question': self.object.pk})


# delete view with login required
class DeleteQuestion(QuestionDispatchMixin, DeleteView, LoginRequiredMixin):
    template_name = 'questions/delete.html'
    model = Question
    success_url = 'accounts:user_questions'
    # get args from url
    pk_url_kwarg = 'question'
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

    # override func success url
    def get_success_url(self):
        # return success url with pk
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.user_id.pk})


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# list all questions
class ListQuestions(ListView):
    template_name = 'questions/all.html'
    model = Question
    paginate_by = 6

    # get queryset
    def get_queryset(self):
        return self.model.objects.all().order_by('-date_created')


# list detail selected question
class DetailQuestion(DetailView):
    template_name = 'questions/detail.html'
    model = Question
    # get args from url
    pk_url_kwarg = 'question'

    # override context_data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(id=self.kwargs['question'])
        # add answers in context
        context['answers'] = list(Answer.objects.filter(question_id=question.id))
        print(context, question.id)
        return context


# ////////////////////////////////////////////////////





