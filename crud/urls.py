from django.conf.urls import url

from crud import views

urlpatterns = [

    url(r'^create$', views.create),
    url(r'^$', views.index),
    url(r'^delete$', views.delete),
    url(r'^update$', views.update),
    url(r'^view$', views.view),

url(r'^edu_create$', views.eduCreate),
url(r'^edu_index$', views.eduIndex),
]