from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import handler404
from home.views import custom_404_view




urlpatterns = [
    path("", views.base, name='home'),
    path("signin",views.signin,name='signin'),
    path("courses",views.courses,name='courses'), 
    path("profile",views.profile,name='profile'),
    path("devop",views.devop, name='devop'),
    path("example",views.example,name='example'), 
    path("student",views.student,name='student'), 
    path("adminportal",views.adminportal,name='adminportal'),
    path("studentrecord",views.studentrecord,name='studentrecord'),
    path("studentlist",views.studentlist,name='studentlist'),
    path("zoom",views.zoom_meeting,name='zoom'), 
    path("timetable",views.time,name='timetable'),
    path("scourse",views.scourse,name='scourse'),
    path("calender" ,views.calender,name='calender'),
    path('logout',views.handlelogout, name = "handlelogout"),
    path('signup', views.handlesignup,name='signup'),
    path('check_username',views.check_username,name='check_username'),
    path('form/<str:username>/',views.form,name='form'),
    path('login',views.handlelogin, name = "handlelogin"),
    path("updateprofile/<int:pk>",views.studentupdate, name = "updateprofile"),
   
]

handler404 = custom_404_view