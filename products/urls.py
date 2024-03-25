from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", view=views.index, name="index"),
]
