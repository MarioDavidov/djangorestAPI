from rest_framework import serializers, status
from rest_framework.response import Response

from companies_api.models import Companies, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
