from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Inventory, EmployeeRequest
from .models import InventoryUsage

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password']

class Inventoryserializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Inventory
        fields = ["id", 'name', 'total', 'description', 'status']

class EmployeeRequestserializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = EmployeeRequest
        fields = ['url', 'employee_id', 'requirements']

class InventoryUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryUsage
        fields = ['url', 'employee', 'inventory']
