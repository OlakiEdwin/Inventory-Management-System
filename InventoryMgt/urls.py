from django.urls import path
from . import views 

#Configurations for the routes 
urlpatterns=[
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('home/', views.home_page)
]