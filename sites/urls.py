from django.conf.urls import url
from sites import views

urlpatterns = [

    url(r'^signup$', views.userRegitser),
    url(r'^login$', views.userLogin),
    url(r'^home$', views.home),
    url(r'^logout$', views.userLogout),

]