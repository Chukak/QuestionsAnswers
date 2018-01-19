from django.conf.urls import url
from .views import CreateUser

app_name = 'auth'

urlpatterns = [
    url(r'create', CreateUser.as_view(), name='register'),
]