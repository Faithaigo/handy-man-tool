from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet,JobViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'clients', ClientsViewSet)
router.register(r'', JobViewSet)

urlpatterns = [
    path('', include(router.urls))
]