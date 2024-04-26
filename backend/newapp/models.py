from django.db import models
from django.contrib.auth.models import User
import uuid

class Employee(models.Model):   
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.employee_name

class Inventory(models.Model):
    id = models.UUIDField(max_length=10, editable=False, default=uuid.uuid4, primary_key=True) # default=uuid.uuid4
    name = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    STATUS_CHOICES = (
        ('Request accept', 'request accept'),
        ('Inprogress', 'inprogress'),
        ('Declined', 'declined'),
    )

    status = models.CharField(max_length=20, choices = STATUS_CHOICES)    

    def __str__(self):
        return self.name

class EmployeeRequest(models.Model):
    employee_id = models.CharField(max_length=20)
    requirements = models.TextField()
    # type = models.CharField(max_length=10)  
    STATUS_CHOICES = (
        ('Request accept', 'request accept'),
        ('Inprogress', 'inprogress'),
        ('Declined', 'declined'),
    )

    STATUS = models.CharField(max_length=20, choices = STATUS_CHOICES)  

    def __str__(self):
        return f"Repository - employee_id: {self.employee_id}, Type: {self.type}"

class InventoryUsage(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['employee', 'inventory']

    def __str__(self):
        return f'{self.employee.username} uses {self.inventory.name}'
