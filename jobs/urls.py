from rest_framework.routers import DefaultRouter
from .views import ClientsViewSets
from django.urls import path, include


router = DefaultRouter()
router.register(r'', ClientsViewSets)

urlpatterns = [
    path('clients/', include(router.urls))
]