from django.conf.urls import url
from .views import CreateQuestion, UpdateQuestion, DeleteQuestion


app_name = 'questions'
urlpatterns = [
    # create question
    url(r'^create/$', CreateQuestion.as_view(), name='create'),
    # update question
    url(r'^(?P<pk>\d+)/update/$', UpdateQuestion.as_view(), name='update'),
    # delete question
    url(r'(?P<pk>\d+)/delete/$', DeleteQuestion.as_view(), name='delete'),
]
