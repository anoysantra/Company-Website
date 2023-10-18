from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),  # This maps the root URL to the homeview function
    # Add other URL patterns as needed
    path('review/', views.review, name='review'),
    path('software_courses/', views.software_course, name='software_course'),
    path('engineering_courses/', views.engineering_course, name='engineering_course'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('placement/',views.placement, name='placement'),
    path('products/',views.products, name='products'),
    path('construction/',views.construction, name='construction'),
    path('construction_services/',views.construction_services, name='construction_services'),
]