from django.urls import include, path
from rest_framework import routers

from .viewsets import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
