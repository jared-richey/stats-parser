from django.urls import path
from stats import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.home, name="home"),
    path("soccer/", views.soccer, name="soccer"),
    path("basketball/", views.basketball, name="basketball"),
    path("baseball/", views.baseball, name="baseball"),
    path("nba/", views.nba, name="nba"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/favicon.ico'))),
]