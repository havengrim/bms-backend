from rest_framework import generics
from .models import CertificateRequest
from .serializers import CertificateRequestSerializer

class CertificateRequestListView(generics.ListAPIView):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertificateRequestSerializer

class CertificateRequestCreateView(generics.CreateAPIView):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertificateRequestSerializer

class CertificateRequestDetailView(generics.RetrieveAPIView):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertificateRequestSerializer
    lookup_field = 'id'

class CertificateRequestUpdateView(generics.UpdateAPIView):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertificateRequestSerializer
    lookup_field = 'id'

class CertificateRequestDeleteView(generics.DestroyAPIView):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertificateRequestSerializer
    lookup_field = 'id'
