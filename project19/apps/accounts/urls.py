from django.conf.urls import url, include

app_name = 'accounts'

urlpatterns = [
    url('(?P<id>)[0-9]', ),
    url('(?P<id>)[0-9]/update', ),
    url('(?P<id>)[0-9]/delete', ),

]
