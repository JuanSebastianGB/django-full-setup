from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request):
    return Response("healthy")


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response("protected")


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "test/",
        lambda request: HttpResponse("Test healthy"),
        name="test",
    ),
    path(
        "protected_path/",
        protected,
        name="protected_path",
    ),
    path(
        "protected_path_v2/",
        ProtectedView.as_view(),
        name="protected_path_v2",
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
