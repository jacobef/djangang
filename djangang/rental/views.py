from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView
import os

from BASE_DIR import generate_geojson
from models import Tool

def home(request):
    return render(request, "rental/home.html")


class ToolCreateView(CreateView):
    model = Tool
    fields = "__all__"
    template_name = "rental/add_listing.html"
    success_url = "/home/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ToolUpdateView(UpdateView):
    model = Tool
    fields = "__all__"
    template_name = "rental/update_listing.html"
    success_url = "/home/"


def tool_search(request):
    return render(request, "rental/tool_search.html")


def local_map(request):

    return render(request, "rental/local_map.html", {"geojson": generate_geojson()})
