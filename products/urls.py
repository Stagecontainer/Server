from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view()), # posts/
    path("requests/", views.RequestListView.as_view()), # posts/requests
]