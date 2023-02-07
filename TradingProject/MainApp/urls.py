from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name = "index"),
    path('View_all_data',views.View_all_data,name = "View_all_data")
]
