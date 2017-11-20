from django.conf.urls import url
from django.views.generic import TemplateView

from .views import MainView


urlpatterns = [
    url(r'^$', MainView.as_view()),

]