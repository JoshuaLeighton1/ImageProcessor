from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success", views.display, name="success"),
    path("display_images", views.display, name="display"),
    path("delete/<int:id>", views.delete, name="delete"),
]
