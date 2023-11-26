from django.urls import path
from users.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView,FeedBackAPIView
from users.views import StudentRegistrationAPIView,StudentVerifyAPIView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('feedback/',FeedBackAPIView.as_view(),name="feedback"),
    path('student/register/',StudentRegistrationAPIView.as_view(),name="student register"),
    path('student/verify/',StudentVerifyAPIView.as_view(),name="student verify")
]