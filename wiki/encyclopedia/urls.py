from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search , name="abcd"),    
    path("new", views.new , name="new"),
    path("created", views.created, name="created"),
    path("edit/<str:title_tbc>",views.edit, name = "edit"),
    path("randompage", views.randompage , name="randompage"),
    path("save" , views.save, name="save"),
    path("<str:entry>", views.entry , name="entry"),
]
