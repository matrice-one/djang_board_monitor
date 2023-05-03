from django.urls import include, path
from rest_framework import routers

from .viewsets import CompanyViewSet
from .views import GetNetworkDataView

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    path('network-data/', GetNetworkDataView.as_view(), name='network-data'),

]
