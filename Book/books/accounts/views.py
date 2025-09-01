from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from accounts.forms import RegisterForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
@login_required()
def profile(request):
    url = reverse("account.profile", args=[request.user.id])
    return redirect(url)


@login_required()
def account_profile(request, id):
    account = get_object_or_404(User, id=id)
    return render(request, "accounts/account_profile_details.html", {"account": account})


class register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = "/accounts/login"


class update_profile(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "accounts/update_profile.html"
    success_url = "/accounts/profile"


class change_password(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = "/accounts/profile"
