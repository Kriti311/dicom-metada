from django.conf import settings
from django.urls import include, path
from .views import register_view, login_view, logout_view, profile_view
from django.conf.urls.static import static

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("", include("dicom.urls")),
]
