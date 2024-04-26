from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, InventoryViewSet, InventoryUsageViewSet, EmployeeRequest

router = routers.DefaultRouter()

router.register(r'employees', UserViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'employeelist', InventoryUsageViewSet)
router.register(r'employeerequest', EmployeeRequest)

urlpatterns = [
    path('', include(router.urls)),
]
