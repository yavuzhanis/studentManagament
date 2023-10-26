from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/", views.base, name="base"),
    #! Login Url
    path('', views.login_view, name='login'),
    path('do_login_view/',views.do_login_view , name='do_login_view'),
    path('do_logout_view/',views.do_logout_view,name='do_logout_view'),
    #! Profile Url
    path('profile',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profile_update'),
    #! Panel url
    path('Hod/Home',Hod_Views.HOME,name='hod_home'),
    #!add Student
    path('Hod/Student/Add',Hod_Views.add_student,name='add_student'),
    path('Hod/Student/View',Hod_Views.view_student,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.edit_student,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.update_student,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.delete_student,name='delete_student'),
    #! staff add
    path('Hod/Staff/Add',Hod_Views.add_staff,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.view_staff,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.edit_staff,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.update_staff,name='update_staff'), 
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.delete_staff,name='delete_staff'),
    #!add course
    path('Hod/Course/Add',Hod_Views.add_course,name='add_course'),
    path('Hod/Course/View',Hod_Views.view_course,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.edit_course,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.update_course,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.delete_course,name='delete_course'),
    #! add subject
    path('Hod/Subject/Add',Hod_Views.add_subject,name='add_subject'),
    path('Hod/Subject/View',Hod_Views.view_subject,name='view_subject'), 
    path('Hod/Subject/Edit/<str:id>',Hod_Views.edit_subject,name='edit_subject'),
    path('Hod/Subject/Update',Hod_Views.update_subject,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.delete_subject,name='delete_subject'),
    #! Session year add
    path('Hod/Session/Add',Hod_Views.add_session,name='add_session'),
    path('Hod/Session/View',Hod_Views.view_session,name='view_session'), 
    path('Hod/Session/Edit/<str:id>',Hod_Views.edit_session,name='edit_session'),
    path('Hod/Session/Update',Hod_Views.update_session,name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_Views.delete_session,name='delete_session'),


    path('Hod/Staff/Send_Notification',Hod_Views.staff_send_notification,name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_Views.staff_save_notification,name='staff_save_notification'),

    #! This is staff url 
    path('Staff/Home',Staff_Views.home,name='staf_home'),

    path('Staff/Notifications',Staff_Views.notifications,name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_Views.staff_notification_mark_as_done,name='staff_notification_mark_as_done'),
    path('Staff/Apply_leave',Staff_Views.staff_apply_leave,name='staff_apply_leave'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
