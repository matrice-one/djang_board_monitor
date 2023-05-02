from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def list(self, request):
        query = request.GET.get('query', '')
        companies = self.filter_queryset(self.get_queryset().filter(name__icontains=query)[:10])
        serializer = self.get_serializer(companies, many=True)
        print(serializer.data)
        return Response(serializer.data)
