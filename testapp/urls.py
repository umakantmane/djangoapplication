from django.conf.urls import url

from testapp import views

urlpatterns = [

    url(r'^hello$', views.helloDjango),
    url(r'^example$', views.example)
]