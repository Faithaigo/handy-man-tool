from rest_framework.routers import DefaultRouter
from tools.views import ToolViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r"", ToolViewSet)

urlpatterns = [
    path("", include(router.urls)),
]