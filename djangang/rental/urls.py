from django.urls import path
from . import views
app_name = "rental"

urlpatterns = [
    path('', views.home),
    path('add/', views.ToolCreateView.as_view(), name="add"),
    path('search/', views.tool_search, name="search"),
    path('map/', views.local_map, name="map"),
    path('tool/<int:pk>', views.ToolUpdateView.as_view()),
]
