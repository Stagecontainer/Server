from django.urls import path
from . import views

urlpatterns = [
    path("", views.practice),
    path("<int:number>/", views.number)
]