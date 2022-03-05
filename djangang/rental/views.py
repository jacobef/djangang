from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView

from rental.models import Tool


def home(request):
    return render(request, "rental/home.html")


class ToolCreateView(CreateView):
    model = Tool
    fields = "__all__"
    template_name = "rental/add_listing.html"
    success_url = "/home/"


class ToolUpdateView(UpdateView):
    model = Tool
    fields = "__all__"
    template_name = "rental/update_listing.html"
    success_url = "/home/"


def tool_search(request):
    return render(request, "rental/tool_search.html")


def local_map(request):
    return render(request, "rental/local_map.html")