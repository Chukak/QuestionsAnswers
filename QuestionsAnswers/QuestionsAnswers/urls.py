"""QuestionsAnswers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # admin site
    url(r'^admin/', admin.site.urls, name='admin'),
    # homepage
    url(r'^', include('apps.homepage.urls'), name='homepage'),
    # authentication
    url(r'^auth/', include('apps.authentication.urls'), name='authentication'),
    # users
    url(r'^users/', include('apps.accounts.urls'), name='users'),
    # questions
    url(r'^questions/', include('apps.questions.urls'), name='questions'),
    # questions and answers
    url(r'^questions/(?P<question>\d+)/answers/', include('apps.answers.urls'), name='answers'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

