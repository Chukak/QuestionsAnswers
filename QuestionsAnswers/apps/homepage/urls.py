from django.conf.urls import url, include
from .views import HomepageView

app_name = 'homepage'

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
]
