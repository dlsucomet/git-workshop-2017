from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [
    # /student/
    url(r'^$', views.index, name='index'),

    url(r'^listofstudents/$', views.listofstudents, name='listofstudents'),

    url(r'^listofcourses/$', views.listofcourses, name='listofcourses'),

    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),

    # /student/student/add/
    url(r'^student/add/$', views.StudentCreate.as_view(), name='student-add'),

    # /student/student/add/
    url(r'^student/course-add/$', views.CourseCreate.as_view(), name='course-add'),

    url(r'^student/grade-add/$', views.AddGrades.as_view(), name='grade-add'),

]