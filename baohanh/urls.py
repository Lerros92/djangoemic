from django.contrib import admin
from django.urls import path
from . import views

app_name = "baohanh"
urlpatterns = [
    path('', views.index, name = "index"),
]
