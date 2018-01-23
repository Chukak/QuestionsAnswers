from django.conf.urls import url
from .views import CreateQuestion, UpdateQuestion, DeleteQuestion, ListQuestions, DetailQuestion


app_name = 'questions'
urlpatterns = [
    # all questions
    url(r'^all/$', ListQuestions.as_view(), name='all'),
    # create question
    url(r'^create/$', CreateQuestion.as_view(), name='create'),
    # update question
    url(r'^(?P<question>\d+)/update/$', UpdateQuestion.as_view(), name='update'),
    # delete question
    url(r'^(?P<question>\d+)/delete/$', DeleteQuestion.as_view(), name='delete'),
    # detail question
    url(r'^(?P<question>\d+)/detail/$', DetailQuestion.as_view(), name='detail'),

]
