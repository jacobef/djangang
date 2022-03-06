from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.ToolCreateView.as_view(), name="add"),
    path('search/', views.tool_search, name="search"),
    path('search/results', views.tool_search_results, name="search-results"),
    path('map/', views.local_map, name="map"),
    path('tool/<int:pk>', views.details, name="details"),
    path('tool/<int:pk>/edit', views.ToolUpdateView.as_view(), name="edit-tool"),
    path('tool/<int:tool_pk>/rent', views.RentalRequestCreateView.as_view(), name="rent-tool"),
    path('requests/inbox', views.rental_requests_inbox, name="requests-inbox"),
    path('requests/outbox', views.rental_requests_outbox, name="requests-outbox"),
    path('requests/<int:pk>/approve', views.approve_rental_request, name="approve-request"),
    path('requests/<int:pk>/reject', views.reject_rental_request, name="reject-request"),
]
