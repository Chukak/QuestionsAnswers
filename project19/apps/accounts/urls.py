from django.conf.urls import url, include
from .views import AccountDetail, AccountUpdate, AccountDelete

app_name = 'accounts'

urlpatterns = [
    # update, delete account, pk=id
    url(r'(?P<pk>\d+)/update/$', AccountUpdate.as_view(), name='update'),
    url(r'(?P<pk>\d+)/delete/$', AccountDelete.as_view(), name='delete'),
    # detail view account
    url(r'(?P<pk>\d+)/$', AccountDetail.as_view(), name='detail'),
]
