from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect("dicom:list")
    return redirect("login")


urlpatterns = [
    path("", home_redirect, name="home"),
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("dicom/", include("dicom.urls", namespace="dicom")),
]
