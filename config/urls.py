from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("core.products.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
