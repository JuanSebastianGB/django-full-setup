from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "test/",
        lambda request: HttpResponse("Hello, World 🕋🕋"),
        name="test",
    ),
]
