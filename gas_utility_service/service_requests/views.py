from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import responses
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.utils.timezone import now


class IsOwnerOrSupport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.customer == request.user

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSupport]

    def get_queryset(self):
        if self.request.user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        request_obj = self.get_object()
        new_status = request.data.get('status')

        if new_status not in dict(ServiceRequest.STATUS_CHOICES):
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

        request_obj.status = new_status
        if new_status in ['RESOLVED', 'CLOSED']:
            request_obj.resolved_at = now()

        request_obj.save()
        return Response(ServiceRequestSerializer(request_obj).data)
