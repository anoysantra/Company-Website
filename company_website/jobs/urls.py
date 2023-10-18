from django.urls import path
from . import views

urlpatterns = [
    path('job_details/',views.post_job, name='post_job'),
    #path('job_details/',views.show_jobs, name='show_job'),
    path('consultancy/',views.consult, name='consultancy'),
]