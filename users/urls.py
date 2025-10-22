# users/urls.py (Create this new file)

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),

    # Make the login page the default home page
    path('', views.login_view, name='home'), 
]