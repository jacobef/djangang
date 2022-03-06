from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView


def index(request):
    if request.user.is_authenticated:
        return render(request, "rental/home.html")
    else:
        return render(request, "accounts/login.html")