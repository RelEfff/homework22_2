from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateView, email_confirm_view, UserUpdateView,
                         UserDetailView, PasswordRecoveryView, CustomLoginView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('password-recovery/', PasswordRecoveryView.as_view(), name='password-recovery'),
    path('email-confirm/<str:token>/', email_confirm_view, name='email-confirm'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
]
