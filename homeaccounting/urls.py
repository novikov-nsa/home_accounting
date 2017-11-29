from django.conf.urls import url
from .views import MainView, NewDocFormView, RegisterFormView, LoginFormView, LogoutView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main-view'),
    url(r'^new/', NewDocFormView.as_view()),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),

]