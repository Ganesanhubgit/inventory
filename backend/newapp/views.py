from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .models import InventoryUsage
from .models import Inventory, EmployeeRequest
from .serializers import GroupSerializer, Userserializer, InventoryUsageSerializer, Inventoryserializer, EmployeeRequestserializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    # permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = Inventoryserializer

class EmployeeRequest(viewsets.ModelViewSet):
    queryset = EmployeeRequest.objects.all()
    serializer_class = EmployeeRequestserializer

class InventoryUsageViewSet(viewsets.ModelViewSet):
    queryset = InventoryUsage.objects.all()
    serializer_class = InventoryUsageSerializer
