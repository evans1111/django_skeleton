from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')

        user.save()
        new_user = authenticate(email=user.email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')
