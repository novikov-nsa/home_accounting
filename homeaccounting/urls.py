from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.main_app, name='main_app'),

]