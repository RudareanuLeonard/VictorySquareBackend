from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("api/", views.api_data_view, name="api_daya_view")
]