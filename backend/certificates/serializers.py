from rest_framework import serializers
from .models import CertificateRequest

class CertificateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateRequest
        fields = '__all__'
        read_only_fields = ['request_number', 'created_at']
