from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "rental/home.html")


def add_listing(request):
    return render(request, "rental/add_listing.html")


def tool_search(request):
    return render(request, "rental/tool_search.html")


def local_map(request):
    return render(request, "rental/local_map.html")