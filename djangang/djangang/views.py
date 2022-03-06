from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, UpdateView


def index(request):
    if request.user.is_authenticated:
        return redirect("rental:home")
    else:
        return redirect("accounts:login")
