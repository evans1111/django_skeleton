from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Makes any view with this only visitable when logged in

def home(request):
    return render(request, "home.html", {})