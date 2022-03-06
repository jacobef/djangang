from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.ToolCreateView.as_view(), name="add"),
    path('search/', views.tool_search, name="search"),
    path('search/results', views.tool_search_results, name="search-results"),
    path('map/', views.local_map, name="map"),
    path('tool/<int:pk>', views.ToolUpdateView.as_view()),
    path('rent/', views.rent, name="rent"),
]
