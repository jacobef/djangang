from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from rental.forms import ToolSearchForm
from rental.models import Tool


def home(request):
    return render(request, "rental/home.html")

def rent(request):
    return render(request, "rental/rent.html")


class ToolCreateView(CreateView):
    model = Tool
    fields = ["name", "location", "brand", "price", "type", "description"]
    template_name = "rental/add_listing.html"
    success_url = reverse_lazy("rental:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ToolUpdateView(UpdateView):
    model = Tool
    fields = ["name", "location", "brand", "price", "type"]
    template_name = "rental/update_listing.html"
    success_url = reverse_lazy("rental:home")


def tool_search(request):
    return render(request, "rental/tool_search.html", {'form': ToolSearchForm()})


def tool_search_results(request):
    matching_tools = Tool.objects.all()
    submitted_form = ToolSearchForm(request.POST)
    if submitted_form.data["by_type"]:
        tool_type = submitted_form.data["by_type"]
        matching_tools = matching_tools.filter(type=tool_type)
    return render(request, "rental/tool_search_results.html", {'tools': matching_tools})


def local_map(request):
    return render(request, "rental/local_map.html")
