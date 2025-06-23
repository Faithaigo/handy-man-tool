from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]