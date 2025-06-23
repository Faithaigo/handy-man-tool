from materials.views import MaterialViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]