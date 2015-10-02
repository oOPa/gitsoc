"""gitoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from . import settings
from gitoc.views import results

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/', results),
    url(r'^(?:index2.html)?$', 'django.contrib.staticfiles.views.serve', kwargs={'path': 'index2.html'}),
    url(r'^asset/',            'django.contrib.staticfiles.views.serve', kwargs={'path': '/asset'}),
    url(r'^(?:index.html)?$', 'django.contrib.staticfiles.views.serve', kwargs={'path': 'index.html'}),
]

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'django.contrib.staticfiles.views.serve'),
)