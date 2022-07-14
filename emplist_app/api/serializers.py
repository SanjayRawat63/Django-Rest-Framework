from unicodedata import name
from rest_framework import serializers

from emplist_app.models import employees

class EmployeeSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=employees
        fields="__all__"