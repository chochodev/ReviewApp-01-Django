from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='/'),
    path('home/', views.homePage, name='home'),
    path('search/', views.searchPage, name='search'),
    path('settings/', views.setting, name='settings'),
    path('anime/<str:pk_test>/', views.lorem, name='lorem'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('user/', views.userPage, name='user'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('createanime/', views.createanime, name='createanime'),
    path('updateanime/<str:pk>/', views.updateanime, name='updateanime'),
    path('deleteanime/<str:pk>/', views.deleteanime, name='deleteanime'),

    path('terms/', views.terms, name='terms'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name="reset_password"),
        
    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_sent.html'),
        name="password_reset_done"),
        
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_form.html'),
        name="password_reset_confirm"),
        
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_success.html'),
        name="password_reset_complete"),
        

]