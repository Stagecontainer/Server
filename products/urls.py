from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view()), # posts/
    path("<int:post_id>/", views.PostDetailView.as_view()), # posts/1
    path("requests/<int:user_id>/", views.RequestListView.as_view()), # posts/requests/4
    path("requests/<int:user_id>/<int:post_id>/", views.RequestPostView.as_view()), # posts/requests/4/1
]