from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from rental.forms import ToolSearchForm, RentalRequestForm
from rental.models import Tool, RentalRequest

from djangang.settings import BASE_DIR

from generate_geojson import generate_geojson



def home(request):
    return render(request, "rental/home.html")

def details(request,pk):
    tool = Tool.objects.filter(pk = pk)
    return render(request, "rental/details.html", {'tool': tool})


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
    fields = ["name", "brand", "price", "type", "location"]
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
    if submitted_form.data["by_name"]:
        tool_name = submitted_form.data["by_name"]
        matching_tools = matching_tools.filter(name=tool_name)
    if submitted_form.data["by_brand"]:
        tool_brand = submitted_form.data["by_brand"]
        matching_tools = matching_tools.filter(brand=tool_brand)
    if submitted_form.data["by_price"]:
        tool_price = submitted_form.data["by_price"]
        matching_tools = matching_tools.filter(price=tool_price)
    return render(request, "rental/tool_search_results.html", {'tools': matching_tools})


def local_map(request):
    return render(request, "rental/local_map.html", {'geojson': generate_geojson()})


def rent_tool(request, pk: int):
    tool = Tool.objects.get(pk=pk)
    form = RentalRequestForm()
    form.instance.tool = tool
    form.instance.recipient = tool.owner
    return render(request, "rental/rent_tool.html", {'tool': tool, 'form': form})


class RentalRequestCreateView(CreateView):
    model = RentalRequest
    fields = ["using_for"]
    template_name = "rental/rent_tool.html"
    success_url = reverse_lazy("rental:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tool"] = Tool.objects.get(pk=self.kwargs["tool_pk"])
        return context

    def form_valid(self, form):
        form.instance.tool = Tool.objects.get(pk=self.kwargs["tool_pk"])
        form.instance.sender = self.request.user
        form.instance.recipient = form.instance.tool.owner
        return super().form_valid(form)


def rental_requests_inbox(request):
    requests_to_me = RentalRequest.objects.filter(recipient=request.user, approved=None, rejected=None)
    return render(request, "rental/requests_inbox.html", {'rental_requests': requests_to_me})


def rental_requests_outbox(request):
    my_requests = RentalRequest.objects.filter(sender=request.user)
    return render(request, "rental/requests_outbox.html", {'rental_requests': my_requests})


def approve_rental_request(request, pk: int):
    rental_request: RentalRequest = RentalRequest.objects.get(pk=pk)
    rental_request.approved = True
    rental_request.save()
    return redirect("rental:home")


def reject_rental_request(request, pk: int):
    rental_request: RentalRequest = RentalRequest.objects.get(pk=pk)
    rental_request.rejected = True
    rental_request.save()
    return redirect("rental:home")
