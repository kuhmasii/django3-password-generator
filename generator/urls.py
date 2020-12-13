from django.urls import path
from . import views

app_name = "generator"

urlpatterns = [
    path("", views.home, name="home"),
    path("gene_pass/", views.password, name="password"),
    path("about/", views.about, name='about'),
    ]

