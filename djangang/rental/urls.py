from django.urls import path
from rental import views


urlpatterns = [
    path('home/', views.home),
    path('add/', views.add_listing),
    path('search/', views.tool_search),
    path('map/', views.local_map),
]