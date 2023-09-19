from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here. In tshi globally apply authentication in Django Rest Framework using the settings.py file directly.


class EmployeeModelViewSetCBV(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
