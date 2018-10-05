from django.conf.urls import url
from student import views

urlpatterns = [

    url(r'^student_exmp$', views.studentExample),
    url(r'^student2$', views.student2),
    url(r'^student_form$', views.createStudent)
]