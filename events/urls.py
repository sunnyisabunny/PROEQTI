from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event-list"),
    path("create/", views.event_create, name="event-create"),
    path("update/<int:pk>/", views.event_update, name="event-update"),
    path("delete/<int:pk>/", views.event_delete, name="event-delete"),
]
