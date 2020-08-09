from django.contrib import admin
from django.urls import path
from . import views

app_name = "baohanh"
urlpatterns = [
    path('', views.index, name = "index"),
    path('addnote', views.addnote, name="addnote"),
    path('additem', views.additem, name="additem"),
    path('notedetail/<int:note_id>', views.notedetail, name="notedetail"),
    path('add', views.add, name="add"),
]
