from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.application_list,
        name='application_list'
    ),

    path(
        'add/',
        views.add_application,
        name='add_application'
    ),

    path(
        'edit/<int:id>/',
        views.edit_application,
        name='edit_application'
    ),

    path(
        'delete/<int:id>/',
        views.delete_application,
        name='delete_application'
    ),

    path(
        'apply/<int:job_id>/',
        views.apply_job,
        name='apply_job'
    ),

    path(
        'my/',
        views.my_applications,
        name='my_applications'
    ),

    path(
        'status/<int:id>/<str:status>/',
        views.update_application_status,
        name='update_application_status'
    ),

]