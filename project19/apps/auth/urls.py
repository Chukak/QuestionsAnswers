from django.conf.urls import url
from .views import CreateUser, LoginUser, logout_user

app_name = 'auth'

urlpatterns = [
    url(r'create', CreateUser.as_view(), name='register'),
    url(r'login', LoginUser.as_view(), name='login'),
    url(r'logout', logout_user, name='logout'),
]