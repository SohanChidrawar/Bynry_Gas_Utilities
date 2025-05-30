from rest_framework import serializers
from .models import ServiceRequest

# Serializer to convert ServiceRequest model into JSON
class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['customer', 'created_at', 'updated_at', 'resolved_at']
