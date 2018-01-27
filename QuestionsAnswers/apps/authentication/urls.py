from django.conf.urls import url
from .views import CreateUser, LoginUser, logout_user

app_name = 'authentication'

urlpatterns = [
    # create account, registration
    url(r'create/$', CreateUser.as_view(), name='register'),
    # login
    url(r'login/$', LoginUser.as_view(), name='login'),
    # logout
    url(r'logout/$', logout_user, name='logout'),
]