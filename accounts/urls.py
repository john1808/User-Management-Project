from django.urls import path
from .views import RegisterView, ProfileView, ResetPasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]
