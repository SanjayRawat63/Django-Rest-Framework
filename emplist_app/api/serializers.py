from unicodedata import name
from rest_framework import serializers

from emplist_app.models import employees

class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    emp_name=serializers.CharField()
    emp_age=serializers.IntegerField()
    emp_designation=serializers.CharField()
    
    def create(self,validated_data):
        return employees.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.emp_name=validated_data.get('emp_name',instance.emp_name)
        instance.emp_age=validated_data.get('emp_age',instance.emp_age)
        instance.emp_designation=validated_data.get('emp_designation',instance.emp_designation)
        instance.save()
        return instance