from unicodedata import name
from rest_framework import serializers

from emplist_app.models import employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields="__all__"