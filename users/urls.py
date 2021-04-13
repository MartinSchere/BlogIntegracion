from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_change_done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset_confirm/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
]
