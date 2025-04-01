"""
URL configuration for brainhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),


    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('newlearner/',views.newlearner,name='newlearner'),
    path('profile/',views.profile,name='profile'),
    path('all_learners/',views.all_learners,name='all_learners'),
    path('learner_profile/',views.learner_profile,name='learner_profile'),

    path('add-category/',views.add_category,name='add-category'),
    path('all-category/',views.all_category,name='all-category'),
    path('edit-category/<int:pk>',views.edit_category,name='edit-category'),
    path('update-category/',views.update_category,name='update-category'),
    path('del-category/<int:pk>',views.del_category,name='del-category'),

    path('add-course/',views.add_course,name='add-course'),
    path('all-course/',views.all_course,name='all-course'),
    path('edit-course/<int:pk>',views.edit_course,name='edit-course'),
    path('del-course/<int:pk>',views.del_course,name='del-course'),
    path('update-course/',views.update_course,name='update-course'),

    path('add-company/',views.add_company,name='add-company'),
    path('all-company/',views.all_company,name='all-company'),
    path('edit-company/<int:pk>',views.edit_company,name='edit-company'),
    path('update-company/',views.update_company,name='update-company'),
    path('delete-company/<int:pk>',views.delete_company,name='delete-company'),

    path('add-enroll-course/<int:pk>',views.add_enroll_course,name='add-enroll-course'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('reset-password/',views.reset_password,name='reset-password'),

    path('all-request',views.all_request,name='all-request'),
    path('accept-request/<int:pk>',views.accept_request,name='accept-request'),
    path('reject-request/<int:pk>',views.reject_request,name='reject-request'),

    #--------------------------------learner side----------------------------------
    path('learner-all-course-list/',views.learner_all_course_list,name='learner-all-course-list'),
    path('learner-all-category/',views.learner_all_category,name='learner-all-category'),

    #------------------------------------------------------------------------------
    path('learner-enroll-course/<int:pk>',views.learner_enroll_course,name='learner-enroll-course'),
    path('learner-add-enroll-course/<int:pk>',views.learner_add_enroll_course,name='learner-add-enroll-course'),
    path('learner-course-vedio/<int:pk>',views.learner_course_vedio,name='learner-course-vedio'),
    path('learner-all-company',views.learner_all_company,name='learner-all-company')





]
#http://127.0.0.1:8000/myapp/home/
#http://127.0.0.1:8000/myapp/about/

#http://127.0.0.1:8000/ #actual url