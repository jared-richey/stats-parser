from django.urls import path
from lines import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.home, name="home"),
    path("soccer/", views.soccer, name="soccer"),
    path("basketball/", views.basketball, name="basketball"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/favicon.ico'))),
]