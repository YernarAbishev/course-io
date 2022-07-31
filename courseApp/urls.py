from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.signUp, name='signUp'),
    path('log-in/', views.logIn, name='logIn'),
    path("logout/", views.logoutUser, name= "logoutUser"),
    path('courses/', views.courseList, name='courseList'),
    path('courses/<slug:slug>/', views.courseList, name='courseListByCategory'),
    path('courses/<slug:slug>/lessons/', views.themeList, name='themeList'),
    path('courses/<slug:slug>/lessons/<int:pk>/', views.themeDetail, name='themeDetail'),
]