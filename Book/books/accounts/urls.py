from django.urls import path, include
from accounts.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("profile/", profile, name="profile"),
    path("profile/<int:id>", account_profile, name="account.profile"),
    path("register/", register.as_view(), name="register"),
    path("update/<int:pk>", update_profile.as_view(), name="update.profile"),
    path("change-password/", change_password.as_view(), name="change.password"),
    path("change-password-done/", PasswordChangeDoneView.as_view(), name="change.password.done"),
]
