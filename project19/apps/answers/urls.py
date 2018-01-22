from django.conf.urls import url
from .views import CreateAnswer, UpdateAnswer, DeleteAnswer


app_name = 'answers'
urlpatterns = [
    # create answer
    url(r'^create/$', CreateAnswer.as_view(), name='create'),
    # update answer
    url(r'^(?P<answer>\d+)/update/$', UpdateAnswer.as_view(), name='update'),
    # delete answer
    url(r'^(?P<answer>\d+)/delete/$', DeleteAnswer.as_view(), name='delete'),
]
