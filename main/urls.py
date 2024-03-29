from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("command-center", views.command_center, name='command-center'),
    path("command-submit", views.command_submit, name='command_submit'),
]