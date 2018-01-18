from django.conf.urls import url, include
from .views import homepage

app_name = 'homepage'

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
]