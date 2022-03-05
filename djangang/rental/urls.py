from django.urls import path
from rental import views


urlpatterns = [
    path('home/', views.home),
    path('add/', views.ToolCreateView.as_view()),
    path('search/', views.tool_search),
    path('map/', views.local_map),
    path('tool/<int:pk>', views.ToolUpdateView.as_view()),
]
