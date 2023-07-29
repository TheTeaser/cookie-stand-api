from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/cookie_stands/", include("cookie_stands.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("cookie_stands/", include("cookie_stands.urls_front")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
