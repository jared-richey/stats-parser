from django.urls import path
from lines import views

urlpatterns = [
    path("", views.home, name="home"),
    path("soccer/", views.soccer, name="soccer"),
    path("basketball/", views.basketball, name="basketball"),
]