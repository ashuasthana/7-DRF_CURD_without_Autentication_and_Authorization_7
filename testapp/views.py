from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
#for authentication these two modules imported
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeModelViewSetCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    #for authentication these two class added
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,]

    