from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib.auth.views import login

from .views import MainView, NewDocFormView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main-view'),
    url(r'^new/', NewDocFormView.as_view()),
    url('^login/$', login, {'redirect_field_name': 'main-view'}),

]