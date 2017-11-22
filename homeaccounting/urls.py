from django.conf.urls import url
from django.views.generic import TemplateView

from .views import MainView, NewDocFormView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main-view'),
    url(r'^new/', NewDocFormView.as_view()),

]